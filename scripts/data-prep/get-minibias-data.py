#!/usr/bin/env python

from AnalysisUtils.diracutils import get_lfns_from_path
import os

outputdir = os.path.expandvars('$AGAMMAD0TOHHPI0ROOT/options/data/minibias/')
if not os.path.exists(outputdir) :
    os.makedirs(outputdir)

get_lfns_from_path('/LHCb/Collision15/Beam6500GeV-VeloClosed-MagDown/RealData/Reco15a/Stripping24/90000000/MINIBIAS.DST',
                   os.path.join(outputdir, 'MiniBias_MagDown_2015.py'))
get_lfns_from_path('/LHCb/Collision15/Beam6500GeV-VeloClosed-MagUp/RealData/Reco15a/Stripping24/90000000/MINIBIAS.DST',
                   os.path.join(outputdir, 'MiniBias_MagUp_2015.py'))
