#!/bin/bash

. ~/lib/bash/lhcb-project-utils/dirac-utils.sh

for year in 2015 2016 2017 2018 ; do
    bkpaths=$(python -c "from StrippingDoc import latest_pp_bkpaths_for_line
for path in latest_pp_bkpaths_for_line('StrippingDstarD0ToHHPi0_pipipi0_M_Line', $year) :
    print path.replace(' ', ''),
")
    for bkpath in $bkpaths ; do
	mag=$(echo $bkpath | grep -o "Mag[A-Za-z]\+\?")
	reco=$(echo $bkpath | grep -o "Reco[0-9a-z]\+\?")
	fname="$AGAMMAD0TOHHPI0ROOT/options/data/real/${reco}_Charm_${mag}.py"
	echo $bkpath
	echo $fname
	#dirac_save_files $fname -B "${bkpath}"
	dirac_get_data_settings $fname
    done
done
