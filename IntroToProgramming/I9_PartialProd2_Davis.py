#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 12:46:42 2019

@author: allisondavis
"""

# Defining things
f=n**2+2*n+1  #f and g are polynomials
g=n**3+4
a_n = lambda n: 1+(f/g)
b=0.5  #b>0 is a constant
b_n = lambda n: 1+b**n

N=100  #total number of terms in the partial product sequence 

#%% First Partial Product
partial_prod1=[]
prod=1
for i in range(1,N+1):
    temp=a_n(i)
    prod*=temp
    partial_prod1.append(prod)
    
print('Last 15: ', partial_prod1[-15:])

#%% Second Partial Product
partial_prod2=[]
prod1=1
for ii in range(1,N+1):
    temp1=b_n(ii)
    prod1*=temp1
    partial_prod2.append(prod1)
    
print('Last 15: ', partial_prod2[-15:])
