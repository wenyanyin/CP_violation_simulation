#!/bin/bash

if [ -z "$(which scons 2> /dev/null)" ] ; then
    sudo apt-get install scons
fi

if [ ! -e ~/lib/mint ] ; then
    mkdir -p ~/lib/mint
fi
export QFT_PATH=~/lib/mint/qft
export MINT2=~/lib/mint/Mint2
export LD_LIBRARY_PATH=${QFT_PATH}/lib:${MINT2}/lib:${LD_LIBRARY_PATH}
cd ~/lib/mint
git clone https://github.com/MannyMoo/qft.git
git clone https://github.com/MannyMoo/Mint2.git
cd qft
scons
cd ../Mint2
scons
cd example
scons
