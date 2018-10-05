#!/usr/bin/env python

from AGammaD0Tohhpi0.data import datalib
import os, ROOT

ROOT.gROOT.SetBatch(True)

tree = datalib.Data_2015_Kpipi0()

outputdir = os.path.join(os.environ['AGAMMAD0TOHHPI0ROOT'], 'scripts', 'deltam', 'slices')
if not os.path.exists(outputdir) :
    os.makedirs(outputdir)

c = ROOT.TCanvas()
for selname, sel in ('-wBDT', datalib.selection), ('-nosel', '1') :
    h = datalib.draw(tree, 'deltam', variableY = 'D0_mass', drawopt = 'colz', selection = sel)
    h.SetStats(False)
    c.SaveAs(os.path.join(outputdir, 'MassVsDeltaM' + selname + '.pdf'))

    deltamdir = os.path.join(outputdir, 'deltamslices' + selname)
    if not os.path.exists(deltamdir) :
        os.makedirs(deltamdir)
    for i in xrange(1, h.GetNbinsX()+1) :
        py = h.ProjectionY('py' + str(i), i, i)
        py.Draw()
        py.SetTitle('{0} < #Deltam [MeV] < {1}'.format(h.GetXaxis().GetBinLowEdge(i),
                                                       h.GetXaxis().GetBinUpEdge(i)))
        c.SaveAs(os.path.join(deltamdir, 'mass-slice-' + str(i).zfill(3) + '.pdf'))

    massdir = os.path.join(outputdir, 'massslices' + selname)
    if not os.path.exists(massdir) :
        os.makedirs(massdir)
    for i in xrange(1, h.GetNbinsY()+1) :
        px = h.ProjectionX('px' + str(i), i, i)
        px.Draw()
        px.SetTitle('{0} < D0 Mass [MeV] < {1}'.format(h.GetYaxis().GetBinLowEdge(i),
                                                          h.GetYaxis().GetBinUpEdge(i)))
        c.SaveAs(os.path.join(massdir, 'deltam-slice-' + str(i).zfill(3) + '.pdf'))
