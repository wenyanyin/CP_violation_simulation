#!/bin/bash

#copy plotTime.C file into 10x10 bins, approximate 100 dirs
echo /nfs/lhcb/malexander01/wenyan/phibin*/ | xargs -n 1 cp -v CP_violation_simulation/scripts/mint/plotTime.C
cd /nfs/lhcb/malexander01/wenyan/
#create output file
touch results.txt

dirnames=${ls phibin*}
for dir in ${dirnames}
do
	root -l $dir/plotTime.C
done

#./ampFit < pipipi0.txt >& stdout &
