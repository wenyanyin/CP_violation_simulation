import os

optsdir = os.path.expandvars('$AGAMMAD0TOHHPI0ROOT/options')
dvdir = os.environ['DAVINCIDEV_PROJECT_ROOT']

def make_job(name, datafile, filesperjob, restrip = True) :
    settings = datafile.replace('.py', '_settings.py')
    if not os.path.exists(settings) :
        settings = datafile.replace('.py', '_DV.py')

    if restrip :
        opts = dict(directory = dvdir,
                    options = [settings,
                               os.path.join(optsdir, 'ntupling/StripKiller.py'),
                               os.path.join(optsdir, 'ntupling/stripping.py'),
                               os.path.join(optsdir, 'ntupling/tuples.py')],
                    platform = 'x86_64-slc6-gcc49-opt')
    else :
        opts = dict(directory = dvdir,
                    options = [settings,
                               os.path.join(optsdir, 'ntupling/tuples.py')],
                    )
        
    j = Job(name = name, splitter = SplitByFiles(filesPerJob = filesperjob),
            application = GaudiExec(**opts),
                                    backend = Dirac(),
                                    outputfiles = [LocalFile('DaVinciTuples.root')],)
    j.application.readInputData(datafile)
    return j

def make_restrip_jobs() :
    jobsdata = []
    for run in '182594', '179101' :
        jdata = make_job('data', os.path.join(optsdir, 'data/real/Reco16_Run' + run + '.py'), 5)
        jdata.application.extraOpts = '''from Gaudi.Configuration import FileCatalog
    FileCatalog().Catalogs += [ 'xmlcatalog_file:$STRIPPINGSELECTIONSROOT/tests/data/Reco16_Run''' + run + '''.xml' ]
    '''
        jobsdata.append(jdata)

    jmcmagdown = make_job('mc-magdown', os.path.join(optsdir, 'data/mc/pipipi0-MagDown-MCFlagged.py'), 40)
    jmcmagup = make_job('mc-magup', os.path.join(optsdir, 'data/mc/pipipi0-MagUp-MCFlagged.py'), 40)

    for j in jobsdata[1], jmcmagup :
        j = j.copy()
        j.splitter = None
        j.backend = Local()
        j.name = j.name + '-test'
        j.inputdata.files = j.inputdata.files[:1]
        j.application.extraOpts += '''
from Configurables import DaVinci
DaVinci().EvtMax = 1000
'''
        j.submit()

def make_jobs() :
    #jmcmagdown = make_job('mc-magdown', '/nfs/lhcb/d2hh01/hhpi0/pipipi0-MagDown-MCFlagged.py', 40, False)
    #jmcmagup = make_job('mc-magup', '/nfs/lhcb/d2hh01/hhpi0/pipipi0-MagUp-MCFlagged.py', 40, False)
    
    for fname in glob.glob(os.path.join(optsdir, 'data/real/Reco16*Charm*')) :
        if '_DV' in fname or '_settings' in fname :
            continue
        j = make_job(os.path.split(fname)[1], fname, 10, False)
        j = j.copy()
        j.splitter = None
        j.backend = Local()
        j.name = j.name + '-test'
        j.inputdata.files = j.inputdata.files[:1]
        j.application.extraOpts += '''
from Configurables import DaVinci
DaVinci().EvtMax = 10000
'''
        j.submit()
