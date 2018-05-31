#!/bin/bash

name=$1
nameupper=$(python -c "print '$name'.upper()")
for f in $(find . -path ./.git -prune -o -type f) ; do
    sed -i "s/TemplateAnalysis/$name/g" $f
    sed -i "s/TEMPLATEANALYSIS/$nameupper/g" $f
done
	
git mv python/TemplateAnalysis python/$name
