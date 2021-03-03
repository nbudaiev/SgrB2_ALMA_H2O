#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np

# More prone to be changed
field = '3' # 3 -- MN, 4 -- MS, 5 -- SDS.
niter=1000
threshold='5.0mJy'
nchan=128 # number of frequency channels to be cleaned per 1 file 

# Change if needed
cell =['0.076arcsec']
imsize=4000
robust=0

# Don't change unless working with other data
vis = '18A-229.sb35069722.eb35251150.58205.383514664354.ms'
spw='53'
specmode='cube'
outframe='LSRK'
restfreq='22.2331141GHz'
perchanweightdensity=True
chanchunks=2
pblimit=-0.0001
weighting='briggs'
interactive=False
savemodel='none'

# I guess this is not very efficient, but will work for now...
if field == '3':
    n_field = 'MN_'
if field == '4':
    n_field = 'MS_'
if field == '5':
    n_field = 'SDS_'
    
n_base='NB_'
n_clean = 'c'+str(niter)+'_'
n_size = 's'+str(imsize)+'_'
n_const = n_base+n_field+n_clean+n_size

starts = np.arange(150, 3071, 128)[:-1] # First non empty channel is 154, but I am including extra 4 channels in the first cube
# Remove the last starting channel as that cube will only include empty channels.


# In[3]:


print('Setup completed')
total_cubes = len(starts)
for i in range(len(starts)):
    start = starts[i]
    n_fchan = str(start)+'-'+str(start+128-1)
    imagename= n_const+n_fchan
    
    print('Imaging cube '+str(i)+' out of '+str(total_cubes))
    print('Frequency channels are: '+n_fchan)
    
    tclean(
    vis=vis
    field=field
    spw=spw
    start=start
    imagename=imagename
    imsize=imsize
    cell=cell
    specmode=specmode
    outframe=outframe
    restfreq=restfreq
    perchanweightdensity=perchanweightdensity
    chanchunks=chanchunks
    pblimit=pblimit
    weighting=weighting
    robust=robust
    niter=niter
    threshold=threshold
    interactive=interactive
    savemodel=savemodel
    nchan=nchan)

