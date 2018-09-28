
'''
Production Info: 
    Configuration Name: LHCb
    Configuration Version: Collision18
    Event type: 90000000
-----------------------
 StepName: Stripping34-DV-v44r4-AppConfig-v3r361 
    StepId             : 133757
    ApplicationName    : DaVinci
    ApplicationVersion : v44r4
    OptionFiles        : $APPCONFIGOPTS/DaVinci/DV-Stripping34-Stripping.py;$APPCONFIGOPTS/DaVinci/DataType-2018.py;$APPCONFIGOPTS/DaVinci/InputType-RDST.py;$APPCONFIGOPTS/DaVinci/DV-RawEventJuggler-0_3-to-4_3.py;$APPCONFIGOPTS/Persistency/Compression-ZLIB-1.py
    DDB                : dddb-20171030-3
    CONDDB             : cond-20180202
    ExtraPackages      : AppConfig.v3r361;SQLDDDB.v7r10;TMVAWeights.v1r10
    Visible            : Y
-----------------------
Number of Steps   153106
Total number of files: 1377954
         BHADRON.MDST:153106
         BHADRONCOMPLETEEVENT.DST:153106
         LOG:153106
         EW.DST:153106
         LEPTONIC.MDST:153106
         CHARM.MDST:153106
         CHARMCOMPLETEEVENT.DST:153106
         DIMUON.DST:153106
         SEMILEPTONIC.DST:153106
Number of events
File Type           Number of events    Event Type          EventInputStat
DIMUON.DST          1244473             90000000            51013252
BHADRONCOMPLETEEVENT.DST1363584             90000000            32878555
CHARMCOMPLETEEVENT.DST1335553             90000000            87790590
EW.DST              1684372             90000000            96910149
CHARM.MDST          8988151             90000000            49556519
SEMILEPTONIC.DST    1767243             90000000            43064904
BHADRON.MDST        7636493             90000000            40213615
LEPTONIC.MDST       10494824            90000000            45183397
Path:  /LHCb/Collision18/Beam6500GeV-VeloClosed-MagDown/Real Data/Reco18/Stripping34
/LHCb/Collision18/Beam6500GeV-VeloClosed-MagDown/Real Data/Reco18/Stripping34/90000000/DIMUON.DST
/LHCb/Collision18/Beam6500GeV-VeloClosed-MagDown/Real Data/Reco18/Stripping34/90000000/BHADRONCOMPLETEEVENT.DST
/LHCb/Collision18/Beam6500GeV-VeloClosed-MagDown/Real Data/Reco18/Stripping34/90000000/CHARMCOMPLETEEVENT.DST
/LHCb/Collision18/Beam6500GeV-VeloClosed-MagDown/Real Data/Reco18/Stripping34/90000000/EW.DST
/LHCb/Collision18/Beam6500GeV-VeloClosed-MagDown/Real Data/Reco18/Stripping34/90000000/CHARM.MDST
/LHCb/Collision18/Beam6500GeV-VeloClosed-MagDown/Real Data/Reco18/Stripping34/90000000/SEMILEPTONIC.DST
/LHCb/Collision18/Beam6500GeV-VeloClosed-MagDown/Real Data/Reco18/Stripping34/90000000/BHADRON.MDST
/LHCb/Collision18/Beam6500GeV-VeloClosed-MagDown/Real Data/Reco18/Stripping34/90000000/LEPTONIC.MDST
'''

from Configurables import DaVinci
from Gaudi.Configuration import importOptions

importOptions('$APPCONFIGOPTS/DaVinci/DataType-2018.py')
DaVinci().InputType = 'MDST'
DaVinci().CondDBtag = 'cond-20180202'
DaVinci().DDDBtag = 'dddb-20171030-3'

