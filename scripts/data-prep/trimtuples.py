#!/usr/bin/env python

import os, ROOT, shutil, glob
from AnalysisUtils.treeutils import copy_tree, is_tfile_ok
from AGammaD0Tohhpi0.data import datadir, datalib
from AnalysisUtils.addmva import make_mva_tree
from AGammaD0Tohhpi0.selection import bdtcut

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

def trim_2015_tuples() :
    files = glob.glob(os.path.join(datadir, 'data', '2015', '*', 'DaVinciTuples_*_Data.root'))
    nfiles = '/' + str(len(files))
    for i, f in enumerate(files) :
        print str(i+1) + nfiles, f
        trim_file(f)

def filter_tuple_mva(inputtree, weightsfile, weightsvar, outputfile, cut) :
    print 'Calculate MVA variable for tree', inputtree.GetName()
    make_mva_tree(inputtree, weightsfile, weightsvar, weightsvar + 'Tree', outputfile + '.weights')
    mvafile = ROOT.TFile.Open(outputfile + '.weights')
    mvatree = mvafile.Get(weightsvar + 'Tree')
    evtlist = ROOT.TEventList('evtlist')
    sel = weightsvar + ' >= ' + str(cut)
    mvatree.Draw('>>' + evtlist.GetName(), sel)
    inputtree.SetEventList(evtlist)
    mvatree.SetEventList(evtlist)
    fout = ROOT.TFile.Open(outputfile, 'recreate')
    print 'Filter tree', inputtree, 'with selection', sel
    treeout = inputtree.CopyTree('')
    mvatreeout = mvatree.CopyTree('')
    fout.Write()
    fout.Close()
    print 'Wrote file', outputfile

def filter_2016_tuples(overwrite = False) :
    weightsfile = os.path.expandvars('$AGAMMAD0TOHHPI0ROOT/tmva/20180702-Lewis/TMVAClassification_BDT_Kpipi0.weights.xml')
    for mag in 'Up', 'Down' :
        print 'Filter Mag' + mag, 'files'
        datainfo = datalib.get_data_info('Data_2016_Kpipi0_Mag' + mag + '_full')
        outputdir = os.path.join(datadir, 'data', '2016', 'mag' + mag.lower())
        if not os.path.exists(outputdir) :
            os.makedirs(outputdir)
        mod2016 = __import__('AGammaD0Tohhpi0.Reco16_Charm_Mag{0}_TupleURLs'.format(mag), fromlist = ['urls'])
        nok = 0
        for lfn, urls in mod2016.urls.items() :
            print 'Process LFN', lfn
            outputfile = os.path.join(outputdir, lfn[1:].replace('/', '_').replace('.root', '_Kpipi0.root'))
            if not overwrite and os.path.exists(outputfile) and is_tfile_ok(outputfile) :
                print 'Output already exists, skipping'
                nok += 1
                continue
            if not urls :
                continue
            ok = False
            # Find a URL that works.
            for url in urls :
                if is_tfile_ok(url) :
                    ok = True
                    break
            if not ok :
                print 'No working URL'
                continue
            inputfile = ROOT.TFile.Open(url)
            tree = inputfile.Get(datainfo['tree'])
            if not tree :
                print 'No tree named {0!r} in file {1}'.format(datainfo['tree'], url)
                continue
            nok += 1
            filter_tuple_mva(tree, weightsfile, 'BDT', outputfile, bdtcut)
        print 'Successfully filtered', str(nok) + '/' + str(len(mod2016.urls)), 'files'

if __name__ == '__main__' :
    filter_2016_tuples()
