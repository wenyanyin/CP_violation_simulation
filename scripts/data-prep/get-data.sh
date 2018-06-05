#!/bin/bash

for mag in Up Down ; do
    bkpath="/LHCb/Collision15/Beam6500GeV-VeloClosed-Mag${mag}/RealData/Reco15a/Stripping24r1/90000000/CHARM.MDST"
    dirac_save_files Reco15a_Charm_Mag${mag}.py -B "$bkpath"
done
