#!/usr/bin/env python

import ROOT
ROOT.gROOT.SetBatch(True)

mp = '((_1_pi#_E + _3_pi0_E)^2 - (_1_pi#_Px + _3_pi0_Px)^2 - (_1_pi#_Py + _3_pi0_Py)^2 - (_1_pi#_Pz + _3_pi0_Pz)^2)'
mm = mp.replace('1_pi#', '2_pi~')
m0 = mp.replace('3_pi0', '2_pi~')

tree = ROOT.TChain('DalitzEventList')
tree.Add("KKpipi_*.root")

canv = ROOT.TCanvas('canv', '', 600, 600)
for name, form in {'dalitz' : mm + ':' + mp,
                   'mplus' : mp,
                   'mminus' : mm,
                   'mzero' : m0}.items() :
    tree.Draw(form, '', 'colz')
    canv.SaveAs(name + '.pdf')
