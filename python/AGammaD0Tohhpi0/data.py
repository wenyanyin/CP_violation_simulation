'''Functions to access all the relevant datasets for the analysis, both TTrees and RooDataSets.'''

import os, ROOT, pprint
from AnalysisUtils.data import DataLibrary
from AGammaD0Tohhpi0.variables import variables

datadir = os.environ.get('AGAMMAD0TOHHPI0DATADIR', 
                         '/nfs/lhcb/d2hh01/hhpi0/')
varnames = ('deltam',)

# All the TTree datasets, the tree names and file names (any number of file names can be given).
datapaths = {'Data_2015_pipipi0' : ('DecayTree', os.path.join(datadir, 'data/DaVinciTuples_S24r1_part_pipipi0.root')),
             'Data_2015_Kpipi0' : ('DecayTree', os.path.join(datadir, 'data/DaVinciTuples_S24r1_part_Kpipi0.root')),
             'Data_2016_pipipi0_HLT2TIS' : ('DecayTree', os.path.join(datadir, 'data/DaVinciTuples_HLT2TIS.root')),
             'MC_2016_pipipi0_HLT2TIS' : ('DecayTree', os.path.join(datadir, 'mc/DaVinciTuples_MC_Matched.root')),
             'MC_2016_pipipi0' : ('DecayTree', os.path.join(datadir, 'mc/DaVinciTuples_MC_S28_Matched.root')),
             }

datalib = DataLibrary(datapaths, variables, varnames)
