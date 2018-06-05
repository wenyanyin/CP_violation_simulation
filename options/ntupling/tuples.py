import sys
sys.path.insert(0, '/cvmfs/lhcb.cern.ch/lib/lhcb/STRIPPING/STRIPPING_v11r5p1/Phys/StrippingSelections/tests/users/')
from StrippingTuple import stripping_tuple_sequence_from_doc
from Configurables import TupleToolTISTOS, LoKi__Hybrid__TupleTool, DaVinci, TupleToolDecayTreeFitter
from StrippingDoc import StrippingDoc

stream = 'Charm.mdst'
if DaVinci().getProp('ProductionType') == 'Stripping' :
    stream = 'CharmCompleteEvent.dst'
elif DaVinci().getProp('Simulation') :
    stream = 'AllStreams.dst'

doc = StrippingDoc('stripping28')
tuples = []
seqs = []
for line in doc.filter_lines(lambda line : line.name.startswith('DstarD0ToHHPi0')) :
    seq = stripping_tuple_sequence_from_doc(line, stream = stream)
    seqs.append(seq)
    tuples.append(seq.Members[-1])
    DaVinci().UserAlgorithms += [seq]
DaVinci(**line.davinci_config(stream))

tttistos = TupleToolTISTOS('tttistos',
                           VerboseHlt2 = True,
                           VerboseHlt1 = True)
tttistos.TriggerList = [line + 'Decision' for line in ['Hlt2CharmHadInclDst2PiD02HHXBDT',
                                                       'Hlt2CharmHadDstp2D0Pip_D02KmKpPi0_Pi0M',
                                                       'Hlt2CharmHadDstp2D0Pip_D02KmKpPi0_Pi0R',
                                                       'Hlt2CharmHadDstp2D0Pip_D02KmPipPi0_Pi0M',
                                                       'Hlt2CharmHadDstp2D0Pip_D02KmPipPi0_Pi0R',
                                                       'Hlt2CharmHadDstp2D0Pip_D02KpPimPi0_Pi0M',
                                                       'Hlt2CharmHadDstp2D0Pip_D02KpPimPi0_Pi0R',
                                                       'Hlt2CharmHadDstp2D0Pip_D02PimPipPi0_Pi0M',
                                                       'Hlt2CharmHadDstp2D0Pip_D02PimPipPi0_Pi0R',
                                                       'Hlt1TrackMVA',
                                                       'Hlt1TwoTrackMVA',
                                                       'Hlt1TrackMVATight',
                                                       'Hlt1TwoTrackMVATight',
                                                       'Hlt1TrackMuon',
                                                       'Hlt1TrackMuonMVA',
                                                       'Hlt1CalibTrackingKK',
                                                       'Hlt1CalibTrackingKPi',
                                                       'Hlt1CalibTrackingKPiDetached',
                                                       'Hlt1CalibTrackingPiPi',]]

for dtt in tuples :
    if '_R_' in dtt.name() :
        dtt.Decay = dtt.Decay.replace('pi0', '( pi0 -> ^gamma ^gamma )')
    dtt.addBranches({'lab0' : dtt.Decay.replace('^', '')})
    dtt.lab0.addTupleTool(tttistos)
    dtt.ToolList += ['TupleToolPropertime',
                     'TupleToolPrimaries',
                     'TupleToolTrackInfo']
    for vtxname, vtx in ('', False), ('_vtx', True) :
        for constraintname, constraints in ('', ['pi0']), ('_D0Mass', ['D0', 'pi0']), ('_DstMass', ['D*(2010)+', 'pi0']), ('_BothMass', ['D0', 'D*(2010)+', 'pi0']) :
            ttdtf = TupleToolDecayTreeFitter('DTF' + vtxname + constraintname)
            ttdtf.constrainToOriginVertex = vtx
            ttdtf.daughtersToConstrain = constraints
            ttdtf.Verbose = True
            dtt.lab0.addTupleTool(ttdtf)

if DaVinci().getProp('Simulation') :
    from Configurables import TupleToolMCTruth, MCTupleToolPrompt
    ttmcmatch = LoKi__Hybrid__TupleTool('ttmcmatch')
    ttmcmatch.Preambulo = ['from LoKiPhysMC.decorators import *', 'from LoKiPhysMC.functions import mcMatch']
    for minus, plus in ('pi', 'pi'), ('K', 'K'), ('K', 'pi') :
        ttmcmatch.Variables['MCMatch_' + minus + plus] = \
            'switch(mcMatch("[ D*(2010)+ ==> ( D0 ==> {minus}-  {plus}+  pi0 )  pi+ ]CC"), 1, 0)'.format(minus = minus, plus = plus)
    ttmctruth = TupleToolMCTruth('ttmctruth')
    ttmctruth.addTupleTool(MCTupleToolPrompt('ttmcprompt'))
    for dtt in tuples :
        dtt.lab0.addTupleTool(ttmcmatch)
        dtt.addTupleTool(ttmctruth)
        
else :
    DaVinci().Lumi = True

DaVinci().TupleFile = 'DaVinciTuples.root'

if stream.endswith('.dst') :
    for dtt in tuples :
        dtt.Inputs[0] = stream.split('.')[0] + '/' + dtt.Inputs[0]
