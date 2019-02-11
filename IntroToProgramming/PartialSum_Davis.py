#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 12:40:26 2019

@author: allisondavis
"""

import numpy as np

#Input value
n=100

#%% First sequence
s1=[]
array1=np.zeros((n))

for i in range(1,n+1):
    s1.append((np.log((i**4)+i+3))/(np.sqrt(i)+3))
for ii in range(len(s1)):
    array1[ii]=sum(s1[0:ii+1])
print('First 15 in Sequence 1:',array1[:15])
print('Last 15 in Sequence 1:',array1[-15:])

#diverges to infinity

#%% Second sequence
s2=[]
array2=np.zeros((n))

for j in range(1,n+1):    
    s2.append((np.exp(j/100))/(j**10))
for jj in range(len(s2)):
    array2[jj]=sum(s2[0:jj+1])
print('First 15 in Sequence 2:',array2[:15])
print('Last 15 in Sequence 2:',array2[-15:])

#converges to 1.01106503?

#%% Third sequence -- sin function
s3=[]
array3=np.zeros((n))

for k in range(1,n+1):
    s3.append((np.sin(k)))
for kk in range(len(s3)):
    array3[kk]=sum(s3[0:kk+1])
print('First 15 in Sequence 3:',array3[:15])
print('Last 15 in Sequence 3:',array3[-15:])

#diverges - oscillates



