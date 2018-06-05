from GaudiScriptBuilder.GangaUtils import BKDataGetter

paths = {'pipipi0-MagDown-MCFlagged' : 'evt+std://MC/2016/27163404/Beam6500GeV-2016-MagDown-Nu1.6-25ns-Pythia8/Sim09c/Trig0x6138160F/Reco16/Turbo03/Stripping28NoPrescalingFlagged/ALLSTREAMS.DST',
         'pipipi0-MagUp-MCFlagged' : 'evt+std://MC/2016/27163404/Beam6500GeV-2016-MagUp-Nu1.6-25ns-Pythia8/Sim09c/Trig0x6138160F/Reco16/Turbo03/Stripping28NoPrescalingFlagged/ALLSTREAMS.DST',
         }

for fname, path in paths.items() :
    getter = BKDataGetter(path)
    datafile = getter.save_data_file(destDir = '.',
                                     fname = fname + '.py')
    print path, ':', datafile
