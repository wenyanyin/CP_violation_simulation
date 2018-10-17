#!/usr/bin/env python

from AnalysisUtils.diracutils import get_access_urls
import os

for mag in 'Up', 'Down' :
    mod2016 = __import__('AGammaD0Tohhpi0.Reco16_Charm_Mag{0}_TupleLFNs'.format(mag), fromlist = ['lfns'])
    urls2016 = __import__('AGammaD0Tohhpi0.Reco16_Charm_Mag{0}_TupleURLs'.format(mag), fromlist = ['urls'])
    for lfn, urls in urls2016.urls.items() :
        if urls and urls[0].startswith('file:') :
            urls2016.urls[lfn] = []
    urls = get_access_urls(mod2016.lfns,
                           outputfile = os.path.join(os.environ['AGAMMAD0TOHHPI0ROOT'], 
                                                     'python/AGammaD0Tohhpi0/Reco16_Charm_Mag{0}_TupleURLs.py'.format(mag)),
                           urls = urls2016.urls)
