#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 11:32:51 2019

@author: allisondavis
"""
import math 
import numpy as np

#define the function
def prime_check(x):
    if x==1:
        return False
    for i in range(2, math.floor(np.sqrt(x))+1):
        if x%i==0:
            return (False)
    return(True)
        

#%% examples
prime_check(55)

#%% determine the nth prime number
n=14

primes=[]
for ii in range(1,1000):
    if prime_check(ii)==True:
        primes.append(ii)
        
# Print the nth prime 
print(primes[n-1], 'is the nth prime number.')

