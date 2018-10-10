# lb-run LHCbDirac/prod dirac-bookkeeping-get-files -B /MC/2015/Beam6500GeV-2015-MagUp-Nu1.6-25ns-Pythia8/Sim09c-ReDecay01/Trig0x411400a2/Reco15a/Turbo02/Stripping24r1NoPrescalingFlagged/27263400/ALLSTREAMS.MDST

from Gaudi.Configuration import *
from GaudiConf import IOHelper
IOHelper('ROOT').inputFiles(
['LFN:/lhcb/MC/2015/ALLSTREAMS.MDST/00075789/0000/00075789_00000001_6.AllStreams.mdst',
 'LFN:/lhcb/MC/2015/ALLSTREAMS.MDST/00075789/0000/00075789_00000002_6.AllStreams.mdst',
 'LFN:/lhcb/MC/2015/ALLSTREAMS.MDST/00075789/0000/00075789_00000003_6.AllStreams.mdst',
 'LFN:/lhcb/MC/2015/ALLSTREAMS.MDST/00075789/0000/00075789_00000004_6.AllStreams.mdst',
 'LFN:/lhcb/MC/2015/ALLSTREAMS.MDST/00075789/0000/00075789_00000005_6.AllStreams.mdst',
 'LFN:/lhcb/MC/2015/ALLSTREAMS.MDST/00075789/0000/00075789_00000006_6.AllStreams.mdst'],
clear=True)
