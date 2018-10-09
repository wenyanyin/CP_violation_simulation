#!/usr/bin/env python

from AnalysisUtils.diracutils import get_bk_decay_paths
import os

evttypes = {27163400 : 'Kpipi0_DecProdCut_PHSP',
            27163401 : 'KKpi0_TightCut',
            27163403 : 'pipipi0_DecProdCut_PHSP',
            27163404 : 'pipipi0_DecProdCut_Dalitz',
            27163405 : 'Kpipi0_DecProdCut_Dalitz',
            27263400 : 'Kpipi0_cocktail_DecProdCut',
            }

for evttype, name in evttypes.items() :
    fname = os.path.expandvars('$AGAMMAD0TOHHPI0ROOT/python/AGammaD0Tohhpi0/MCBKPaths_{0}.py'.format(name))
    get_bk_decay_paths(evttype, exclusions = ('GAUSSHIST', 'STRIP'), outputfile = fname)
