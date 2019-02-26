#!/bin/bash

#copy plotTime.C file into 10x10 bins, approximate 100 dirs
echo /nfs/lhcb/malexander01/wenyan/phibin*/ | xargs -n 1 cp -v ~/CP_violation_simulation/scripts/mint/plotTime.C
cd /nfs/lhcb/malexander01/wenyan/
#create output file
rm results.txt
touch results.txt

dirnames=$(ls $path)

for dir in ${dirnames}
do
	cd $dir
	#output the value of phi and qoverp into results.txt
	#phi
	tail -n 2 pipipi0.txt | head -n 1 | tr -cd "[0-9] . -" >> ../results.txt
	#qoverp
	tail -n 1 pipipi0.txt | tr -cd "[0-9] ." >> ../results.txt

	root -b -q plotTime.C >stdout
	#Extract number of the standard output: AGAMMA
	tail -n 2 stdout | head -n 1 | tr -cd "[0-9] ." >> ../results.txt
	#Extract number of the standard output: AGAMMAERROR
	sed -n '$p' stdout | tr -cd "[0-9] ." >> ../results.txt
	echo -e "\n" >> ../results.txt
	cd ..
done

#./ampFit < pipipi0.txt >& stdout &

#Extrcat the second last row
#cat file | sed -n '2p' or cat file |head -n 2|tail -n 1
#Extract last line of the file
#sed -n '$p' file
