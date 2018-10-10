# lb-run LHCbDirac/prod dirac-bookkeeping-get-files -B /MC/2012/Beam4000GeV-2012-MagDown-Nu2.5-Pythia8/Sim08c/Digi13/Trig0x409f0045/Reco14a/Stripping20NoPrescalingFlagged/27163401/ALLSTREAMS.DST

from Gaudi.Configuration import *
from GaudiConf import IOHelper
IOHelper('ROOT').inputFiles(
['LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00031647/0000/00031647_00000001_1.allstreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00031647/0000/00031647_00000002_1.allstreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00031647/0000/00031647_00000003_1.allstreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00031647/0000/00031647_00000004_1.allstreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00031647/0000/00031647_00000005_1.allstreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00031647/0000/00031647_00000006_1.allstreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00031647/0000/00031647_00000007_1.allstreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00031647/0000/00031647_00000008_1.allstreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00031647/0000/00031647_00000009_1.allstreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00031647/0000/00031647_00000010_1.allstreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00031647/0000/00031647_00000011_1.allstreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00031647/0000/00031647_00000012_1.allstreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00031647/0000/00031647_00000013_1.allstreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00031647/0000/00031647_00000014_1.allstreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00031647/0000/00031647_00000015_1.allstreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00031647/0000/00031647_00000016_1.allstreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00031647/0000/00031647_00000017_1.allstreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00031647/0000/00031647_00000018_1.allstreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00031647/0000/00031647_00000019_1.allstreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00031647/0000/00031647_00000020_1.allstreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00031647/0000/00031647_00000021_1.allstreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00031647/0000/00031647_00000022_1.allstreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00031647/0000/00031647_00000023_1.allstreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00031647/0000/00031647_00000024_1.allstreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00031647/0000/00031647_00000025_1.allstreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00031647/0000/00031647_00000026_1.allstreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00031647/0000/00031647_00000027_1.allstreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00031647/0000/00031647_00000028_1.allstreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00031647/0000/00031647_00000029_1.allstreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00031647/0000/00031647_00000030_1.allstreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00031647/0000/00031647_00000031_1.allstreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00031647/0000/00031647_00000032_1.allstreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00031647/0000/00031647_00000033_1.allstreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00031647/0000/00031647_00000034_1.allstreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00031647/0000/00031647_00000035_1.allstreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00031647/0000/00031647_00000036_1.allstreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00031647/0000/00031647_00000037_1.allstreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00031647/0000/00031647_00000038_1.allstreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00031647/0000/00031647_00000039_1.allstreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00031647/0000/00031647_00000040_1.allstreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00031647/0000/00031647_00000041_1.allstreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00031647/0000/00031647_00000042_1.allstreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00031647/0000/00031647_00000043_1.allstreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00031647/0000/00031647_00000044_1.allstreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00031647/0000/00031647_00000045_1.allstreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00031647/0000/00031647_00000046_1.allstreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00031647/0000/00031647_00000047_1.allstreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00031647/0000/00031647_00000048_1.allstreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00031647/0000/00031647_00000049_1.allstreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00031647/0000/00031647_00000050_1.allstreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00031647/0000/00031647_00000051_1.allstreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00031647/0000/00031647_00000052_1.allstreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00031647/0000/00031647_00000053_1.allstreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00031647/0000/00031647_00000054_1.allstreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00031647/0000/00031647_00000055_1.allstreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00031647/0000/00031647_00000056_1.allstreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00031647/0000/00031647_00000057_1.allstreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00031647/0000/00031647_00000058_1.allstreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00031647/0000/00031647_00000059_1.allstreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00031647/0000/00031647_00000060_1.allstreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00031647/0000/00031647_00000061_1.allstreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00031647/0000/00031647_00000062_1.allstreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00031647/0000/00031647_00000063_1.allstreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00031647/0000/00031647_00000064_1.allstreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00031647/0000/00031647_00000065_1.allstreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00031647/0000/00031647_00000066_1.allstreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00031647/0000/00031647_00000067_1.allstreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00031647/0000/00031647_00000068_1.allstreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00031647/0000/00031647_00000069_1.allstreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00031647/0000/00031647_00000070_1.allstreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00031647/0000/00031647_00000071_1.allstreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00031647/0000/00031647_00000072_1.allstreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00031647/0000/00031647_00000073_1.allstreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00031647/0000/00031647_00000074_1.allstreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00031647/0000/00031647_00000075_1.allstreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00031647/0000/00031647_00000076_1.allstreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00031647/0000/00031647_00000077_1.allstreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00031647/0000/00031647_00000078_1.allstreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00031647/0000/00031647_00000079_1.allstreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00031647/0000/00031647_00000080_1.allstreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00031647/0000/00031647_00000081_1.allstreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00031647/0000/00031647_00000082_1.allstreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00031647/0000/00031647_00000083_1.allstreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00031647/0000/00031647_00000084_1.allstreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00031647/0000/00031647_00000085_1.allstreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00031647/0000/00031647_00000086_1.allstreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00031647/0000/00031647_00000087_1.allstreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00031647/0000/00031647_00000088_1.allstreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00031647/0000/00031647_00000089_1.allstreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00031647/0000/00031647_00000090_1.allstreams.dst',
 'LFN:/lhcb/MC/2012/ALLSTREAMS.DST/00031647/0000/00031647_00000091_1.allstreams.dst'],
clear=True)