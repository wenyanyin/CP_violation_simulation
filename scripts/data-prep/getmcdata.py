#!/usr/bin/env python

from AnalysisUtils.diracutils import get_bk_decay_paths, get_lfns
import os

evttypes = {27163400 : 'Kpipi0_DecProdCut_PHSP',
            27163401 : 'KKpi0_TightCut',
            27163403 : 'pipipi0_DecProdCut_PHSP',
            27163404 : 'pipipi0_DecProdCut_Dalitz',
            27163405 : 'Kpipi0_DecProdCut_Dalitz',
            27263400 : 'Kpipi0_cocktail_DecProdCut',
            }

def get_paths() :
    for evttype, name in evttypes.items() :
        fname = os.path.expandvars('$AGAMMAD0TOHHPI0ROOT/python/AGammaD0Tohhpi0/MCBKPaths_{0}.py'.format(name))
        get_bk_decay_paths(evttype, exclusions = ('GAUSSHIST', 'STRIP', 'LDST', 'XDIGI', 'Stripping24[^r]', 'Stripping28[^r]'),
                           outputfile = fname)

def get_data() :
    for evttype, name in evttypes.items() :
        modname = 'AGammaD0Tohhpi0.MCBKPaths_{0}'.format(name)
        mod = __import__(modname, fromlist = ['decaypaths'])
        for year, paths in mod.decaypaths.items() :
            if not year in ('2011', '2012', '2015', '2016', '2017', '2018') :
                continue
            for path in paths :
                fname = os.path.expandvars('$AGAMMAD0TOHHPI0ROOT/options/data/mc/{0}_{1}_{2}.py'.format(name, year, path['path'][1:].replace('/', '_')))
                get_lfns('-B', path['path'], outputfile = fname)

if __name__ == '__main__' :
    #get_paths()
    get_data()
