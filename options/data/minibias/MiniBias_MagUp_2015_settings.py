
'''
Production Info: 
    Configuration Name: LHCb
    Configuration Version: Collision15
    Event type: 90000000
-----------------------
 StepName: Stripping24-DV-v38r1p1-AppConfig-v3r249 
    StepId             : 128893
    ApplicationName    : DaVinci
    ApplicationVersion : v38r1p1
    OptionFiles        : $APPCONFIGOPTS/DaVinci/DV-Stripping24-Stripping.py;$APPCONFIGOPTS/DaVinci/DataType-2015.py;$APPCONFIGOPTS/DaVinci/InputType-RDST.py;$APPCONFIGOPTS/DaVinci/DV-RawEventJuggler-0_3-to-4_2.py;$APPCONFIGOPTS/Persistency/Compression-ZLIB-1.py
    DDB                : dddb-20150724
    CONDDB             : cond-20150828
    ExtraPackages      : AppConfig.v3r249;SQLDDDB.v7r10
    Visible            : Y
-----------------------
Number of Steps   121933
Total number of files: 1707062
         RADIATIVE.DST:121933
         MDST.DST:121933
         BHADRON.MDST:121933
         MINIBIAS.DST:121933
         PID.MDST:121933
         BHADRONCOMPLETEEVENT.DST:121933
         EW.DST:121933
         LEPTONIC.MDST:121933
         LOG:121933
         CALIBRATION.DST:121933
         CHARM.MDST:121933
         CHARMCOMPLETEEVENT.DST:121933
         DIMUON.DST:121933
         SEMILEPTONIC.DST:121933
Number of events
File Type           Number of events    Event Type          EventInputStat
MINIBIAS.DST        371                 90000000            60608
Path:  /LHCb/Collision15/Beam6500GeV-VeloClosed-MagUp/Real Data/Reco15a/Stripping24
/LHCb/Collision15/Beam6500GeV-VeloClosed-MagUp/Real Data/Reco15a/Stripping24/90000000/MINIBIAS.DST
'''

from Configurables import DaVinci
from Gaudi.Configuration import importOptions

importOptions('$APPCONFIGOPTS/DaVinci/DataType-2015.py')
DaVinci().InputType = 'DST'
DaVinci().CondDBtag = 'cond-20150828'
DaVinci().DDDBtag = 'dddb-20150724'

