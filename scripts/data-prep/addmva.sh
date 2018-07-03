#!/bin/bash

mva=BDT
#inputfile=/afs/phas.gla.ac.uk/user/m/malexander/public_html/teaching/project-students/2018-Theodora/DaVinciTuples_RealData.root
#inputtree="DecayTree"
#outputtree=/afs/phas.gla.ac.uk/user/m/malexander/public_html/teaching/project-students/2018-Theodora/DaVinciTuples_RealData_BDT.root

#inputfile=\$AGAMMAD0TOHHPI0DATADIR/data/DaVinciTuples_S24r1_part.root
#inputtree="DstarD0ToHHPi0_pipipi0_R_LineTuple/DecayTree"
#outputfile=data/DaVinciTuples_S24r1_part_BDT.root

#inputfile=\$AGAMMAD0TOHHPI0DATADIR/data/DaVinciTuples_S24r1_part.root
#inputtree="DstarD0ToHHPi0_Kpipi0_R_LineTuple/DecayTree"
#outputfile=\$AGAMMAD0TOHHPI0DATADIR/data/DaVinciTuples_S24r1_part_BDT_Kpipi0.root

#inputfile=\$AGAMMAD0TOHHPI0DATADIR/mc/DaVinciTuples_MC_S28_Matched_pipipi0.root
#inputtree=DecayTree
#outputfile=\$AGAMMAD0TOHHPI0DATADIR/mc/DaVinciTuples_MC_S28_Matched_pipipi0_BDT.root
#outputtree=BDTTree

#../../../run python \$ANALYSISUTILSROOT/python/AnalysisUtils/addmva.py --inputfile ${inputfile/\$/\$} --inputtree "$inputtree" --outputfile $outputfile --outputtree BDTTree --weightsfile \$AGAMMAD0TOHHPI0ROOT/tmva/20180327-Theodora/TMVAClassification_${mva}.weights.xml --weightsvar ${mva} && \
#../../../run \$ANALYSISUTILSROOT/scripts/mergetrees.py tmp.root ${inputfile/\$/\$} $inputtree ${outputfile/\$/\$} $outputtree && \
#../../../run mv tmp.root ${inputfile/\$/\$}

inputtree="DstarD0ToHHPi0_Kpipi0_R_LineTuple/DecayTree"
for inputfile in $(ls $AGAMMAD0TOHHPI0DATADIR/data/2015/*/DaVinciTuples_*.root) ; do
    echo $inputfile
    outputfile=${inputfile/\.root/_Kpipi0_BDT.root}
    echo $outputfile
    ../../../run python \$ANALYSISUTILSROOT/python/AnalysisUtils/addmva.py --inputfile ${inputfile/\$/\$} --inputtree "$inputtree" --outputfile $outputfile --outputtree BDTTree --weightsfile \$AGAMMAD0TOHHPI0ROOT/tmva/20180702-Lewis/TMVAClassification_BDT_Kpipi0.weights.xml --weightsvar ${mva}
done
