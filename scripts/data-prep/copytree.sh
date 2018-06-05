#!/bin/bash

copyTree.py --inFile DaVinciTuples.root --inTree DstarD0ToHHPi0_pipipi0_R_LineTuple/DecayTree --outFile DaVinciTuples_HLT2TIS.root --selection "lab0_Hlt1Phys_TOS && lab0_Hlt2Phys_TIS"
