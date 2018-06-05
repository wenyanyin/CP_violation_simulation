bkglum = 128.245 # /nb
nmcgen = 1995881 + 2000074
dstxsecinacc = 784e3 # nb
dstd0pibf = .677
d0pipipi0bf = 0.0147

mclum = nmcgen/dstxsecinacc/dstd0pibf/d0pipipi0bf
print 'mclum', mclum, '/nb'
print 'signal weight', bkglum/mclum
print 'n signal in bkg', bkglum * dstxsecinacc * dstd0pibf * d0pipipi0bf
