#!/usr/bin/env python

from AGammaD0Tohhpi0.data import datalib
from AnalysisUtils.treeutils import tree_iter
total = 0.
for year in '2016', :
    for mag in 'Up', 'Down' :
        t = datalib.get_data('Data_2016_Mag' + mag + '_lumi')
        lumiiter = tree_iter(t, 'IntegratedLuminosity')
        lumi = sum(lumiiter)
        print year, 'Mag' + mag, ':', '{0:.3f}'.format(lumi/1e6)
        total += lumi

print 'total:', '{0:.3f}'.format(total/1e6)
