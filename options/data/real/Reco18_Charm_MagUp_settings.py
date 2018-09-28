
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
Number of Steps   64041
Total number of files: 576369
         BHADRON.MDST:64041
         BHADRONCOMPLETEEVENT.DST:64041
         EW.DST:64041
         LEPTONIC.MDST:64041
         LOG:64041
         CHARM.MDST:64041
         CHARMCOMPLETEEVENT.DST:64041
         DIMUON.DST:64041
         SEMILEPTONIC.DST:64041
Number of events
File Type           Number of events    Event Type          EventInputStat
DIMUON.DST          9969                90000000            398111
BHADRONCOMPLETEEVENT.DST16261               90000000            398111
EW.DST              40714               90000000            2295653
CHARMCOMPLETEEVENT.DST7098                90000000            474332
SEMILEPTONIC.DST    73145               90000000            1768751
BHADRON.MDST        241079              90000000            1305302
CHARM.MDST          13528               90000000            75409
LEPTONIC.MDST       248202              90000000            1076719
Path:  /LHCb/Collision18/Beam6500GeV-VeloClosed-MagUp/Real Data/Reco18/Stripping34
/LHCb/Collision18/Beam6500GeV-VeloClosed-MagUp/Real Data/Reco18/Stripping34/90000000/DIMUON.DST
/LHCb/Collision18/Beam6500GeV-VeloClosed-MagUp/Real Data/Reco18/Stripping34/90000000/BHADRONCOMPLETEEVENT.DST
/LHCb/Collision18/Beam6500GeV-VeloClosed-MagUp/Real Data/Reco18/Stripping34/90000000/EW.DST
/LHCb/Collision18/Beam6500GeV-VeloClosed-MagUp/Real Data/Reco18/Stripping34/90000000/CHARMCOMPLETEEVENT.DST
/LHCb/Collision18/Beam6500GeV-VeloClosed-MagUp/Real Data/Reco18/Stripping34/90000000/SEMILEPTONIC.DST
/LHCb/Collision18/Beam6500GeV-VeloClosed-MagUp/Real Data/Reco18/Stripping34/90000000/BHADRON.MDST
/LHCb/Collision18/Beam6500GeV-VeloClosed-MagUp/Real Data/Reco18/Stripping34/90000000/CHARM.MDST
/LHCb/Collision18/Beam6500GeV-VeloClosed-MagUp/Real Data/Reco18/Stripping34/90000000/LEPTONIC.MDST
'''

from Configurables import DaVinci
from Gaudi.Configuration import importOptions

importOptions('$APPCONFIGOPTS/DaVinci/DataType-2018.py')
DaVinci().InputType = 'MDST'
DaVinci().CondDBtag = 'cond-20180202'
DaVinci().DDDBtag = 'dddb-20171030-3'

