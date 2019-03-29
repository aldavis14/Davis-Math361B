#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 17:50:36 2019

@author: allisondavis
"""

# Define the function.   
def divisors(n):
    divisors = []
    for i in range(1,n):
        if n%i==0:
            divisors.append(i)
    return divisors

#%% Find amicable numbers up to some upper bound N.
N = 2000
amicable = []

for i in range(1,N):
    a = sum(divisors(i))
    if sum(divisors(a)) == i and a!=i:
        amicable.append(i)
print(set(amicable))
