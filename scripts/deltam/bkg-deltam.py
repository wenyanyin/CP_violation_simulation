#!/usr/bin/env python

from AGammaD0Tohhpi0.data import datalib
import ROOT
ROOT.gROOT.SetBatch(True)
tdata = datalib.Data_2015_Kpipi0()
tmb = datalib.MiniBias_2015()

idata = 0
c = ROOT.TCanvas()
h = ROOT.TH1F('h', '', 100, 140, 170)
for i in xrange(min(tmb.GetEntries(), tdata.GetEntries())) :
    tmb.GetEntry(i)
    tdata.GetEntry(i)
    pD = ROOT.TLorentzVector(tdata.lab1_PX, tdata.lab1_PY, tdata.lab1_PZ, tdata.lab1_PE)
    ppi = ROOT.TLorentzVector(tmb.piplus_PX, tmb.piplus_PY, tmb.piplus_PZ, tmb.piplus_PE)
    pDst = ROOT.TLorentzVector(pD)
    pDst += ppi
    h.Fill(pDst.M() - pD.M())
h.Draw()
c.SaveAs('bkg-deltam.pdf')
