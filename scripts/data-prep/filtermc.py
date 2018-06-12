#!/bin/env python

from AGammaD0Tohhpi0.data import datalib, datadir
from AGammaD0Tohhpi0.selection import *
import ROOT

fmc = ROOT.TFile.Open('$AGAMMAD0TOHHPI0DATADIR/mc/DaVinciTuples_MC_S28.root')
tmc = fmc.Get('DstarD0ToHHPi0_pipipi0_R_LineTuple/DecayTree')

fout = ROOT.TFile.Open('$AGAMMAD0TOHHPI0DATADIR/mc/DaVinciTuples_MC_S28_Matched_pipipi0.root', 'recreate')
tout = tmc.CopyTree(MC_sel_pipi_R)
tout.Write()
fout.Close()
