from numpy import *
import csv
from pandas import *
from fuzzywuzzy import fuzz

def duplicate(file,nfile,fuzlev=68,skip=0):
    print ('Hold your horses...This will take ahwile!')
    g=pandas.read_csv(file)
    rw=g.shape[0]
    cl=g.shape[1]
    errors=zeros(rw)
    f=g.ix[:,2].str.lower()
    for index in range(rw):
        if index==rw/10:
            print 'Look at you! You are 10% of the way there.'
        if index==rw/8:
            print 'Only 20%'
        if index==(rw*3)/10:
            print 'A whopping 30% complete'
        if index==(rw*2)/5:
            print '40%'
        if index==(42*rw)/100:
            print '42%?'
        if index==rw/4:
            print ('25% Complete')
        if index==rw/2:
            print 'Halfway there'
        if index==(rw*3)/4:
            print '75% baby'
        if index==(19*rw)/20:
            print 'Almost There....ALMOST THERE'
        for c in range(index+1, rw):
            if fuzz.ratio(f[index],f[c])>=fuzlev:
                errors[index]=1
                errors[c]=1
    errors=DataFrame(errors)
    yay=concat([g,errors],axis=1)
    yay.to_csv(nfile)

