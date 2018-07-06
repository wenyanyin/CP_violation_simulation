#!/usr/bin/env python

from AGammaD0Tohhpi0.data import datalib
import ROOT
from AnalysisUtils.treeutils import TreeFormula

ROOT.gROOT.SetBatch(True)
tdata = datalib.Data_2015_Kpipi0()
tmb = datalib.MiniBias_2015()

idata = 0
c = ROOT.TCanvas()
h = ROOT.TH1F('h', '', 100, 140, 170)

lab1_P = tuple(TreeFormula(tdata, 'lab1_P' + comp) for comp in 'XYZE')
piplus_P = tuple(TreeFormula(tmb, 'piplus_P' + comp) for comp in 'XYZE')

for i in xrange(min(tmb.GetEntries(), tdata.GetEntries())) :
    tmb.GetEntry(i)
    tdata.GetEntry(i)
    pD = ROOT.TLorentzVector(*tuple(p() for p in lab1_P))
    ppi = ROOT.TLorentzVector(*tuple(p() for p in piplus_P))
    pDst = ROOT.TLorentzVector(pD)
    pDst += ppi
    h.Fill(pDst.M() - pD.M())
h.Draw()
c.SaveAs('bkg-deltam.pdf')
