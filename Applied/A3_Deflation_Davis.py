#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 12:06:27 2019

@author: allisondavis
"""
import numpy as np

# Define polynomials f and g. The ith element of the list is the coefficient for the x^i term of the polynomial.
x = [-1, 0, 0, 1]
y = [2, 1]

#%%
def clean_poly(p):
    highest_deg = len(p) - 1   
    for ii in range(len(p)-1,-1,-1):
        #print('highest', highest_deg)
        #print('pii', p[ii])
        if np.abs(p[ii]) > 1e-15:
            break
        else:
            highest_deg -= 1
            
        del p[highest_deg+1:]
    return p

# Degree of polynomial:
def degree(x):
    return len(x)-1

# Divide leading terms of polynomials:
def divide_leading(a, b):
    new_degree = degree(a)-degree(b)
    poly = [0]*(new_degree+1)
    poly[-1] = a[-1]/b[-1]
    return poly

# Add polynomials:
def add(a, b):
    bigger = max(len(a), len(b))
    added = [0]*bigger
    for i in range(len(a)):
        added[i] = a[i]
    for ii in range(len(b)):
        added[ii] += b[ii]
    return added

def subtract(a, b):
    bigger = max(len(a), len(b))
    sub = [0]*bigger
    for i in range(len(a)):
        sub[i] = a[i]
    for ii in range(len(b)):
        sub[ii] -= b[ii]
    return clean_poly(sub)

def multiply_leading(a, b):
    div = divide_leading(a, b)
    new_degree = degree(div)+degree(b)
    poly = [0]*(new_degree+1)
    for i in range(len(b)):
        poly[-i-1] = div[-1]*b[-i-1]
    return poly
    
def div_alg(f, g):
    q = [0]
    r = list(f)
    while r != [0] and degree(g)<=degree(r):
        q = add(q, divide_leading(r, g))
        r = subtract(r, multiply_leading(r, g))
        #print('changed q: '+str(q))
        #print('changed r: '+str(r))
    print('(q, r): ')
    return (q, r)

#%% Test Division Algorithm
div_alg(x, y)



