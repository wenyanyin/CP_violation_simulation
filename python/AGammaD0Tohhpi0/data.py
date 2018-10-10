'''Functions to access all the relevant datasets for the analysis, both TTrees and RooDataSets.'''

import os, ROOT, pprint, glob
from AnalysisUtils.data import DataLibrary
from AGammaD0Tohhpi0.variables import variables
import Reco16_Charm_MagUp_TupleURLs, Reco16_Charm_MagDown_TupleURLs

datadir = os.environ.get('AGAMMAD0TOHHPI0DATADIR', 
                         '/nfs/lhcb/d2hh01/hhpi0/')
varnames = ('deltam',)

# All the TTree datasets, the tree names and file names (any number of file names can be given).
datapaths = {'Data_2015_pipipi0' : ('DecayTree', os.path.join(datadir, 'data/DaVinciTuples_S24r1_part_pipipi0.root')),
             'Data_2015_Kpipi0' : ('DecayTree', os.path.join(datadir, 'data/DaVinciTuples_S24r1_part_Kpipi0.root')),
             'Data_2016_pipipi0_HLT2TIS' : ('DecayTree', os.path.join(datadir, 'data/DaVinciTuples_HLT2TIS.root')),
             'MC_2016_pipipi0_HLT2TIS' : ('DecayTree', os.path.join(datadir, 'mc/DaVinciTuples_MC_Matched.root')),
             'MC_2016_pipipi0' : ('DecayTree', os.path.join(datadir, 'mc/DaVinciTuples_MC_S28_Matched_pipipi0.root')),
             'MiniBias_2015' : ('pions_tuple_sel/DecayTree',) + tuple(glob.glob(os.path.join(datadir, '../minibias/2015/*/DVTuples*.root'))),
             'Data_2016_Kpipi0_MagUp_full' : ('DstarD0ToHHPi0_Kpipi0_R_LineTuple/DecayTree',)\
                 + tuple(Reco16_Charm_MagUp_TupleURLs.urls),
             'Data_2016_Kpipi0_MagDown_full' : ('DstarD0ToHHPi0_Kpipi0_R_LineTuple/DecayTree',)\
                 + tuple(Reco16_Charm_MagDown_TupleURLs.urls),
             'Data_2016_Kpipi0_MagUp' : ('DecayTree', os.path.join(datadir, 'data/Data_2016_Kpipi0_MagUp.root')),
             'Data_2016_Kpipi0_MagDown' : ('DecayTree', os.path.join(datadir, 'data/Data_2016_Kpipi0_MagDown.root')),
             }

selection = 'BDT > -0.1'

datalib = DataLibrary(datapaths, variables, varnames = varnames, selection = selection)
