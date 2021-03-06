# lb-run LHCbDirac/prod dirac-bookkeeping-get-files -B /MC/2012/Beam4000GeV-2012-MagUp-Nu2.5-Pythia8/Sim08e/Digi13/Trig0x409f0045/Reco14a/Stripping20r0p2NoPrescalingFlagged/27163403/ALLSTREAMS.DST

from Gaudi.Configuration import *
from GaudiConf import IOHelper
IOHelper('ROOT').inputFiles(
['LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034127/0000/00034127_00000001_2.AllStreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034127/0000/00034127_00000003_2.AllStreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034127/0000/00034127_00000004_2.AllStreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034127/0000/00034127_00000005_2.AllStreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034127/0000/00034127_00000006_2.AllStreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034127/0000/00034127_00000008_2.AllStreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034127/0000/00034127_00000009_2.AllStreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034127/0000/00034127_00000011_2.AllStreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034127/0000/00034127_00000012_2.AllStreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034127/0000/00034127_00000013_2.AllStreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034127/0000/00034127_00000014_2.AllStreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034127/0000/00034127_00000015_2.AllStreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034127/0000/00034127_00000016_2.AllStreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034127/0000/00034127_00000017_2.AllStreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034127/0000/00034127_00000018_2.AllStreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034127/0000/00034127_00000019_2.AllStreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034127/0000/00034127_00000020_2.AllStreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034127/0000/00034127_00000021_2.AllStreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034127/0000/00034127_00000022_2.AllStreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034127/0000/00034127_00000024_2.AllStreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034127/0000/00034127_00000025_2.AllStreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034127/0000/00034127_00000027_2.AllStreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034127/0000/00034127_00000028_2.AllStreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034127/0000/00034127_00000029_2.AllStreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034127/0000/00034127_00000030_2.AllStreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034127/0000/00034127_00000033_2.AllStreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034127/0000/00034127_00000034_2.AllStreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034127/0000/00034127_00000036_2.AllStreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034127/0000/00034127_00000037_2.AllStreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034127/0000/00034127_00000039_2.AllStreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034127/0000/00034127_00000040_2.AllStreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034127/0000/00034127_00000042_2.AllStreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034127/0000/00034127_00000044_2.AllStreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034127/0000/00034127_00000046_2.AllStreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034127/0000/00034127_00000048_2.AllStreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034127/0000/00034127_00000049_2.AllStreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034127/0000/00034127_00000050_2.AllStreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034127/0000/00034127_00000052_2.AllStreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034127/0000/00034127_00000053_2.AllStreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00034127/0000/00034127_00000054_2.AllStreams.dst'],
clear=True)
