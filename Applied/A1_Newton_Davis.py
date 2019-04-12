#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 12:03:45 2019

@author: allisondavis
"""

import numpy as np
import math

# Create Variables.
N = 100
TOL = 1e-1 
z0 = math.pi/4  #initial iterate of Newton's method
Iterations = np.zeros([0,2])

# Equation 1:
#f = lambda x: 1/100 * ( x**4 + (np.exp(1)-2-np.sqrt(2))*x**3 + (2*np.sqrt(2)-np.sqrt(2)*np.exp(1)-3-2*np.exp(1))*x**2 + (2*np.sqrt(2)*np.exp(1)+3*np.sqrt(2)-3*np.exp(1))*x + 3*np.sqrt(2)*np.exp(1) )
#f_prime = lambda x: 1/100 * ( 4*x**3 + 3*(np.exp(1)-2-np.sqrt(2))*x**2 + 2*(2*np.sqrt(2)-np.sqrt(2)*np.exp(1)-3-2*np.exp(1))*x + (2*np.sqrt(2)*np.exp(1)+3*np.sqrt(2)-3*np.exp(1)))

# Equation 2:
f = lambda x: math.tan(x) - x - 2
f_prime = lambda x: (1/math.cos(x))**2 - 1

while len(Iterations) < N:
    z1 = z0 - (f(z0) / f_prime(z0))
    t = abs(z1-z0)
    Iterations = np.vstack([Iterations, np.array([z1, t])])
    if t < TOL:
        print('Iterations have stopped due to reaching tolerance.')
        break
    z0 = z1
if len(Iterations) == N:
    print('Iterations have stopped due to reaching the max number of iterations.')
print('Array with iterations and spacing between them:')
print(Iterations)