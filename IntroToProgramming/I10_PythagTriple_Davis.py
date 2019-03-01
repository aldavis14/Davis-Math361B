#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 20:00:25 2019

@author: allisondavis
"""
#import libraries
import numpy as np

#%% Create the triples
triples = np.zeros([0,4])

for i in range(1,500):
    for j in range(i,500):
        for k in range(j,500):
            if i**2+j**2 == k**2:
                triples = np.vstack( [triples, np.array([i,j,k,i+j+k])])


#%% Find the triple for which a+b+c=1026
print(triples[np.where(triples[:,3]==1026)],'is the triple that we wanted to find.')