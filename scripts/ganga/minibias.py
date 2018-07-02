import os, glob, ROOT

dvdir = os.environ['DAVINCIDEV_PROJECT_ROOT']
optsdir = os.path.expandvars('$AGAMMAD0TOHHPI0ROOT/options/')

seed = 894982
rand = ROOT.TRandom3(seed)
frac = 0.05

for f in glob.glob(os.path.join(optsdir, 'data/minibias/*.py')) :
    if 'settings' in f :
        continue
    j = Job(name = f.split(os.sep)[-1],
            application = GaudiExec(directory = dvdir,
                                    options = [os.path.join(optsdir, 'ntupling/minibias.py'),
                                               f.replace('.py', '_settings.py')],
                                    ),
            backend = Dirac(),
            splitter = SplitByFiles(filesPerJob = 10, ignoremissing = True),
            outputfiles = [LocalFile('DVTuples.root')],
            )
    j.application.readInputData(f)
    j.inputdata.files = filter(lambda f : rand.Rndm() < frac, j.inputdata.files)

    j = j.copy()
    j.name = 'test_' + j.name
    j.backend = Local()
    j.splitter = None
    j.inputdata.files = j.inputdata.files[:2]
    j.application.extraOpts += '\nfrom Configurables import DaVinci\nDaVinci().EvtMax = 1000\n'
