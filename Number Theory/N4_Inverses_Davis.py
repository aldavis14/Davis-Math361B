#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 11:42:30 2019

@author: allisondavis
"""

# input variable
m = 5

# find which elements have multiplicative inverses
inverses=[]
for i in range(0,m):
    for k in range(0,m):
        if (i*k)%m==1:
            inverses.append(i)
print('Elements that have a multiplicative inverse: ', inverses)
print('How many elements?', len(inverses))