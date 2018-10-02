import sys
sys.path.insert(0, '/cvmfs/lhcb.cern.ch/lib/lhcb/STRIPPING/STRIPPING_v11r5p1/Phys/StrippingSelections/tests/users/')
from StrippingTuple import stripping_tuple_sequence_from_doc
from Configurables import TupleToolTISTOS, LoKi__Hybrid__TupleTool, DaVinci, TupleToolDecayTreeFitter, \
    TupleToolPropertime, TupleToolANNPID
from StrippingDoc import StrippingDoc

stream = 'Charm.mdst'
if DaVinci().getProp('ProductionType') == 'Stripping' :
    stream = 'CharmCompleteEvent.dst'
elif DaVinci().getProp('Simulation') :
    stream = 'AllStreams.dst'

doc = StrippingDoc('stripping28')
tuples = []
seqs = []
for line in doc.filter_lines(lambda line : (line.name.startswith('DstarD0ToHHPi0') 
                                            and not 'KK' in line.name 
                                            and not 'WIDEMASS' in line.name)) :
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

tttime = TupleToolPropertime('tttime')
tttime.FitToPV = True

ttpid = TupleToolANNPID('ttpid')
ttpid.ANNPIDTunes = ['MC15TuneV1']

for dtt in tuples :
    if '_R_' in dtt.name() :
        dtt.Decay = dtt.Decay.replace('pi0', '( pi0 -> ^gamma ^gamma )')
    dtt.addBranches({'lab0' : dtt.Decay.replace('^', '')})
    dtt.lab0.addTupleTool(tttistos)
    dtt.addTupleTool(tttime)
    dtt.ToolList.remove('TupleToolANNPID')
    dtt.ToolList.remove('TupleToolPid')
    dtt.addTupleTool(ttpid)
    dtt.ToolList += ['TupleToolPrimaries',
                     'TupleToolTrackInfo']
    for name, attrs in {'DTF' : {'constrainToOriginVertex' : False,
                                 'daughtersToConstrain' : ['pi0']},
                        'DTF_vtx' : {'constrainToOriginVertex' : True,
                                     'daughtersToConstrain' : ['pi0']},
                        'DTF_vtx_D0Mass' : {'constrainToOriginVertex' : True,
                                            'daughtersToConstrain' : ['pi0', 'D0']}}.items() :
        ttdtf = TupleToolDecayTreeFitter(name, **attrs)
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
