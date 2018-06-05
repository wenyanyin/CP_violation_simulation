#!/bin/bash

#CMTCONFIG=${CMTCONFIG/gcc62/gcc49} ./DaVinciDev_v41r4p4/run gaudirun.py --option="from Configurables import DaVinci;DaVinci().EvtMax = 1000" pipipi0-MagDown-MCFlagged-1File.py pipipi0-MagDown-MCFlagged_DV.py stripping.py tuples.py >& stdout
CMTCONFIG=${CMTCONFIG/gcc62/gcc49} ./DaVinciDev_v41r4p4/run gaudirun.py --option="from Configurables import DaVinci;DaVinci().EvtMax = 1000" Reco16_Run182594.py Reco16_Run182594_DV.py stripping.py tuples.py >& stdout
