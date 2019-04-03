#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 13:03:19 2019

@author: allisondavis
"""
import math 
import numpy as np

#%% Create list of primes to upper bound p.
p = 100

def prime_check(x):
    if x==1:
        return False
    for i in range(2, math.floor(np.sqrt(x))+1):
        if x%i==0:
            return (False)
    return(True)

primes = []
for i in range(1, p+1):
    if prime_check(i)==True:
        primes.append(i)

#%% Create table that stores the value of p and the # of quadratic residues in Zp.
    # Create a table that stores whether -1 is a quadratic residue in Zp.
count = np.zeros([0,2])
neg_one = np.zeros([0,2])

for m in primes:
    quad_residues=[]
    for j in range(0, m):
        for k in range(0, m):
            if j == ((k**2)%m):
                quad_residues.append(j)
    if m-1 in quad_residues:
        neg_one = np.vstack([neg_one, np.array([m,True])])
    else:
        neg_one = np.vstack([neg_one, np.array([m,False])])
    count = np.vstack([count, np.array([m,len(set(quad_residues))])])
print('Prime p, Number of Quadratic Residues in Zp: \n'+str(count))
print('Prime p, Is -1 a Quadratic Residue? \n'+str(neg_one))

