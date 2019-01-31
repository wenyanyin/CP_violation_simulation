Assuming root environment is running (source thisroot.sh)
cd AGammaD0Tohhpi0/scripts/mint
./install-mint.sh

uninstall mint
./unistall-mint.sh

This will install the packages qft++ and Mint2 in the directory ~/lib/mint. It'll also install the 'scons' package that's required to build them. You should only need to do this once.

Then, to run the generation software, in the directory AGammaD0Tohhpi0/scripts/mint do:

source mint-env.sh

to configure the environment for Mint - you'll need to do this once per session. Then build the generator programme with:

scons

You'll need to do this any time you make a change to the source code in ampFit.cpp. Then you can run it with

./ampFit < pipipi0.txt >& stdout
