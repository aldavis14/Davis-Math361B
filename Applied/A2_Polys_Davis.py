#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 13:04:29 2019

@author: allisondavis
"""

# Create Polynomial.
p = [-9, 2, 0, -8, 4]
# The ith element of the list is the coefficient for the x^i term of the polynomial.

#%%
# Evaluate the polynomial p at a given value x.
def poly(x):
    total = 0
    for i in range(len(p)):
        term = p[i]*(x**i)
        total += term
    return total

# Take the derivative of a polynomial x. 
def derivative(x):
    d = []
    for j in range(len(x)):
        d.append(j*x[j])
    if d[0]==0:
        del d[0]
    return d

# Take the integral of a polynomial x.
def integral(x): 
    l = ['c']
    for k in range(len(x)):
        l.append(x[k]/(k+1))
    return l

#%%
# Evaluate polynomial p at a point c:
print('Polynomial evaluated at a point c: '+str(poly(0)))

# Find derivative of p:
print('The derivative of p is: '+str(derivative(p)))

# Find integral of p:
print('The integral of p is: '+str(integral(p)))
