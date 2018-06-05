from StrippingSelections import buildersConf
from StrippingSelections.Utils import  buildStreams

conf = buildersConf()
conf = {'DstarD0ToHHPi0' : conf['DstarD0ToHHPi0']}

conf['DstarD0ToHHPi0']['STREAMS'] = ['CharmCompleteEvent']

hhpi0conf = conf['DstarD0ToHHPi0']['CONFIG']
hhpi0conf['D0_APT'] = 700
hhpi0conf['Kaon_PIDK'] = 0.
hhpi0conf['Kaon_PT'] = 250
hhpi0conf['Kaon_TRGHOSTPROB'] = .5
hhpi0conf['Pi0M_PT'] = 250
hhpi0conf['Pi0R_PT'] = 250
hhpi0conf['Pion_PIDK'] = 5
hhpi0conf['Pion_PT'] = 250
hhpi0conf['Pion_TRGHOSTPROB'] = .5
hhpi0conf['Slowpion_PIDe'] = 10
hhpi0conf['Slowpion_PT'] = 250
hhpi0conf['Slowpion_TRGHOSTPROB'] = .5
hhpi0conf['Daughter_PT'] = 250
hhpi0conf['Daughter_IPChi2'] = 16
hhpi0conf['HH_DOCAChi2'] = 20
hhpi0conf['HH_VtxChi2NDF'] = 10
hhpi0conf['HH_FDChi2'] = 30.
hhpi0conf['D0_VtxChi2NDF'] = 10
hhpi0conf['Dst_DOCAChi2'] = 20
hhpi0conf['Dst_VtxChi2NDF'] = 10
hhpi0conf['D0_DIRA'] = -1.

streams = buildStreams(conf)

#define stream names
leptonicMicroDSTname   = 'Leptonic'
charmMicroDSTname      = 'Charm'
pidMicroDSTname        = 'PID'
bhadronMicroDSTname    = 'Bhadron'
mdstStreams = [ leptonicMicroDSTname,charmMicroDSTname,pidMicroDSTname,bhadronMicroDSTname ]
dstStreams  = [ "BhadronCompleteEvent", "CharmCompleteEvent", "Dimuon",
                "EW", "Semileptonic", "Calibration", "MiniBias", "Radiative" ]

stripTESPrefix = 'Strip'

from StrippingConf.Configuration import StrippingConf
from Configurables import ProcStatusCheck

sc = StrippingConf( Streams = streams,
                    MaxCandidates = 2000,
                    MaxCombinations = 10000000,
                    AcceptBadEvents = False,
                    BadEventSelection = ProcStatusCheck(),
                    TESPrefix = stripTESPrefix,
                    ActiveMDSTStream = True,
                    Verbose = True,
                    DSTStreams = dstStreams,
                    MicroDSTStreams = mdstStreams )

from Configurables import DaVinci
from Gaudi.Configuration import MessageSvc
MessageSvc().Format = "% F%60W%S%7W%R%T %0W%M"

DaVinci().HistogramFile = 'DV_stripping_histos.root'
DaVinci().PrintFreq = 1000
DaVinci().appendToMainSequence( [ sc.sequence() ] )
DaVinci().ProductionType = "Stripping"
