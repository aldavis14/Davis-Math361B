#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 14:29:39 2019

@author: allisondavis
"""

import numpy as np
from functools import reduce

n=150


#%% First sequence
p1=[]
array_p1=np.zeros((n))

for i in range(2,n+1):
    p1.append(((i**3)-1)/((i**3)+1))
for ii in range(len(p1)):
    array_p1[ii]=reduce(lambda a,b: a*b, (p1[0:ii+1]))
print('First 15 in Sequence 1:',array_p1[:15])
print('Last 15 in Sequence 1:',array_p1[-15:])

#%% Second sequence
p2=[]
array_p2=np.zeros((n))

for j in range(1,n+1):    
    p2.append((np.exp(j/100))/(j**10))
for jj in range(len(p2)):
    array_p2[jj]=reduce(lambda a,b: a*b, (p2[0:jj+1]))
print('First 15 in Sequence 2:',array_p2[:15])
print('Last 15 in Sequence 2:',array_p2[-15:])

#Approaches 0??

#%% Third sequence -- my creation
p3=[]
array3=np.zeros((n))

for k in range(1,n+1):
    p3.append################3
for kk in range(len(p3)):
    array_p3[kk]=reduce(lambda a,b: a*b, (p3[0:kk+1]))
print('First 15 in Sequence 3:',array_p3[:15])
print('Last 15 in Sequence 3:',array_p3[-15:])








