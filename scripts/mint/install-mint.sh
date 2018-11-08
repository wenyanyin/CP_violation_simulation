#!/bin/bash

if [ -z "$(which scons 2> /dev/null)" ] ; then
    # For Ubuntu/Debian, assuming you have root access.
    if [ ! -z "$(which apt-get 2> /dev/null)" ] ; then
	sudo apt-get install scons
    else
	if [ ! -e ~/lib/scons ] ; then
	    mkdir ~/lib/scons
	fi
	cd ~/lib/scons
	fname=scons-3.0.1.tar.gz
	wget http://prdownloads.sourceforge.net/scons/$fname
	tar -xzf $fname
	cd ${fname/\.tar\.gz/}
	python setup.py install --prefix=$HOME
    fi
fi
if [ -z "$(echo $PATH | grep $HOME/bin)" ] ; then
    export PATH=$HOME/bin:$PATH
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
