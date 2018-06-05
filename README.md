# Template analysis structure in the LHCb software structure

The code is organised as an LHCb CMake project, so you can build & run it in an LHCb application. It requires AnalysisUtils. Eg,

```
lb-dev DaVinci/v43r1
cd DaVinciDev_v43r1
git clone ssh://git@gitlab.cern.ch:7999/malexand/AGammaD0Tohhpi0.git
git clone ssh://git@gitlab.cern.ch:7999/malexand/AnalysisUtils.git
make
```

Then `./run <whatever>` will execute whatever command in the analysis environment, so you can use any of the python modules.

# Directory structure

## options

Python LFN datasets & ntupling options.

## python/AGammaD0Tohhpi0

Shared python modules for core functionality, eg, accessing ntuples/RooDataSets, building fit models, plotting utils.

## scripts

Scripts containing main code for the analysis. These should be fairly minimal with all the functionality living in `python/AGammaD0Tohhpi0`.

## tmva

Where to keep the output of TMVA trainings (.root and .xml files).
