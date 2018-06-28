
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
Number of Steps   177950
Total number of files: 2491300
         RADIATIVE.DST:177950
         MDST.DST:177950
         BHADRON.MDST:177950
         MINIBIAS.DST:177950
         PID.MDST:177950
         BHADRONCOMPLETEEVENT.DST:177950
         EW.DST:177950
         LEPTONIC.MDST:177950
         LOG:177950
         CALIBRATION.DST:177950
         CHARM.MDST:177950
         CHARMCOMPLETEEVENT.DST:177950
         DIMUON.DST:177950
         SEMILEPTONIC.DST:177950
Number of events
File Type           Number of events    Event Type          EventInputStat
SEMILEPTONIC.DST    630                 90000000            59891
Path:  /LHCb/Collision15/Beam6500GeV-VeloClosed-MagDown/Real Data/Reco15a/Stripping24
/LHCb/Collision15/Beam6500GeV-VeloClosed-MagDown/Real Data/Reco15a/Stripping24/90000000/SEMILEPTONIC.DST
'''

from Configurables import DaVinci
from Gaudi.Configuration import importOptions

importOptions('$APPCONFIGOPTS/DaVinci/DataType-2015.py')
DaVinci().InputType = 'DST'
DaVinci().CondDBtag = 'cond-20150828'
DaVinci().DDDBtag = 'dddb-20150724'

