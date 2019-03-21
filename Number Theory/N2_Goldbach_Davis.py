#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 13:13:39 2019

@author: allisondavis
"""

import math 
import numpy as np

def prime_check(x):
    if x==1:
        return False
    for i in range(2, math.floor(np.sqrt(x))+1):
        if x%i==0:
            return (False)
    return(True)
#%% Create list of primes and list of twice squares
primes=[]
for ii in range(1,10000):
    if prime_check(ii)==True:
        primes.append(ii)

twice_square=[]
for i in range(0, 500):
    twice_square.append(2*i**2)
    
# Add them together in all possible ways
sums=[]
for prime in primes:
    for square in twice_square:
        sums.append(prime+square)

#%% Create list of odd composites
odd_composite=[]
for kk in range(2,10000):
    if kk not in primes and kk%2 != 0:
        odd_composite.append(kk)
       
#%% Check to see where the conjuecture fails
for n in odd_composite:
    if n not in sums:
        print(str(n)+' FAILS!!!!')
        break
