#!/usr/bin/env python

import os, ROOT, shutil, glob
from AnalysisUtils.treeutils import copy_tree
from AGammaD0Tohhpi0.data import datadir

def trim_file(infile) :
    removebranches = ('lab[0-9]_MC12TuneV[0-9]_ProbNN',
                      'lab[0-9]_ProbNN',
                      'lab[0-9]_PID',
                      'lab0_DTF_vtx_DstMass',
                      'lab0_DTF_vtx_BothMass',
                      'lab0_DTF_DstMass',
                      'lab0_DTF_D0Mass',
                      'lab0_DTF_BothMass',
                      'lab[0-9]_hasMuon',
                      'lab[0-9]_isMuon',
                      'lab[0-9]_hasRich',
                      'lab[0-9]_UsedRich',
                      'lab[0-9]_RichAbove',
                      'lab[0-9]_hasCalo')

    outfile = ROOT.TFile.Open(infile + '.trim', 'recreate')
    infile = ROOT.TFile.Open(infile)
    for k in infile.GetListOfKeys() :
        if 'KK' in k.GetName() or 'WIDEMASS' in k.GetName() :
            continue
        outfile.mkdir(k.GetName())
        outfile.cd(k.GetName())
        for tname in infile.Get(k.GetName()).GetListOfKeys() :
            print 'Copy tree', k.GetName() + '/' + tname.GetName()
            tcopy = copy_tree(infile.Get(k.GetName() + '/' + tname.GetName()), removebranches = removebranches)
            tcopy.Write()
        outfile.cd()

    outfile.Close()
    infile.Close()
    shutil.move(outfile.GetName(), infile.GetName())

if __name__ == '__main__' :
    files = glob.glob(os.path.join(datadir, 'data', '2015', '*', 'DaVinciTuples_*_Data.root'))
    nfiles = '/' + str(len(files))
    for i, f in enumerate(files) :
        print str(i+1) + nfiles, f
        trim_file(f)
