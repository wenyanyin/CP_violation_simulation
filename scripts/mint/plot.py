#!/usr/bin/env python

import ROOT
ROOT.gROOT.SetBatch(True)
ROOT.TH1.SetDefaultSumw2()

mp = '((_1_pi#_E + _3_pi0_E)^2 - (_1_pi#_Px + _3_pi0_Px)^2 - (_1_pi#_Py + _3_pi0_Py)^2 - (_1_pi#_Pz + _3_pi0_Pz)^2)'
mm = mp.replace('1_pi#', '2_pi~')
m0 = mp.replace('3_pi0', '2_pi~')

mpi0 = 134.5
mpip = 139.6
mdz = 1864.84
mcmin = mpi0**2 + mpip**2 - 50
mcmax = mdz**2 - mcmin + 100
mzmin = 2*mpip**2 - 50
mzmax = mdz**2 - mzmin + 100

tree = ROOT.TChain('DalitzEventList')
tree.Add("pipipi0_*.root")

canv = ROOT.TCanvas('canv', '', 600, 600)
plots = {}
for name, form in {'dalitz' : '{0} : {1} >> h(100, {2}, {3}, 100, {2}, {3})'.format(mm, mp, mcmin, mcmax),
                   'mplus' : '{0} >> h(100, {1}, {2})'.format(mp, mcmin, mcmax),
                   'mminus' : '{0} >> h(100, {1}, {2})'.format(mm, mcmin, mcmax),
                   'mzero' : '{0} >> h(100, {1}, {2})'.format(m0, mzmin, mzmax)}.items() :
    plots[name] = {}
    for tag in '-1', '+1' :
        tree.Draw(form, 'tag == ' + tag, 'colz')
        h = ROOT.gDirectory.Get('h')
        h.SetName(name + '_tag_' + str(tag))
        plots[name][tag] = h
        canv.SaveAs(name + '_tag_' + tag + '.pdf')
        nbins = 41
        binwidth = 0.1
        #nbins = 2
        #binwidth = 5.
        for i in xrange(nbins) :
            time = i*binwidth
            tree.Draw(form, 'tag == ' + tag + ' && {0} < decaytime && decaytime <= {1}'.format(time, time+binwidth), 'colz')
            canv.SaveAs('timebins/' + name + '_tag_' + tag + '_timebin_' + str(i).zfill(2) + '.pdf')

for name, hp, hm in (('mplus', plots['mplus']['+1'], plots['mminus']['-1']),
                     ('mminus', plots['mminus']['+1'], plots['mplus']['-1']),
                     ('mzero', plots['mzero']['+1'], plots['mzero']['-1'])) :
    hp.SetLineColor(ROOT.kBlack)
    hp.Draw()
    hm.SetLineColor(ROOT.kBlue)
    hm.Draw('same')
    canv.SaveAs(name + '_comparetags.pdf')
