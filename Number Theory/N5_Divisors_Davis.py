#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 17:50:43 2019

@author: allisondavis
"""

# Define the function.
def divisors(n):
    divisors = []
    for m in range(1, n):
        for k in range(1, n+1):
            if m*k==n:
                divisors.append(m)
    print(divisors)

#%% Print out divisors of a number.
divisors(40)
