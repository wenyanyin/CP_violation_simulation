'''Functions to access all the relevant datasets for the analysis, both TTrees and RooDataSets.'''

import os, ROOT, pprint
from AnalysisUtils.data import DataLibrary
from AGammaD0Tohhpi0.variables import variables

datadir = os.environ.get('AGAMMAD0TOHHPI0DATADIR', 
                         'root://eoslhcb.cern.ch//eos/lhcb/user/u/user/data/')
varnames = ('mass', 'decaytime', 'XcIPX', 'XcIPY')

# All the TTree datasets, the tree names and file names (any number of file names can be given).
datapaths = {'LTUNB_Lc_2015' : ('XcTopKpiTuple/DecayTree', os.path.join(datadir, 'Lc_2015.root')),
             }

datalib = DataLibrary(datapaths, variables, varnames)
