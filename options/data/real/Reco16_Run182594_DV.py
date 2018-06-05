from Configurables import DaVinci
from Gaudi.Configuration import importOptions, FileCatalog

DaVinci().DataType = '2016'
DaVinci().InputType = 'RDST'
DaVinci().DDDBtag = 'dddb-20150724'
DaVinci().CondDBtag = 'cond-20170325'

importOptions('$APPCONFIGOPTS/DaVinci/DV-RawEventJuggler-0_3-to-4_2.py')

FileCatalog().Catalogs += [ 'xmlcatalog_file:$STRIPPINGSELECTIONSROOT/tests/data/Reco16_Run182594.xml' ]
