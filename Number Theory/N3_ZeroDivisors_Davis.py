#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 11:42:30 2019

@author: allisondavis
"""

# input variable
m = 8

zero_divisors=[]
for i in range(1,m):
    for k in range(1,m):
        if (i*k)%m==0:
            zero_divisors.append(i)
print('The zero divisors are : ', set(zero_divisors))
print('How many? ', len(set(zero_divisors)))