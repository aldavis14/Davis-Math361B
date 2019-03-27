#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 17:50:43 2019

@author: allisondavis
"""

# Define the function.
def divisors(n):
    divisors = []
    for i in range(1,n):
        if n%i==0:
            divisors.append(i)
    print(divisors)

#%% Print out divisors of a number.
divisors(40)
