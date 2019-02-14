#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 12:11:38 2019

@author: allisondavis
"""

#function that generates fibonacci sequence based on starting two numbers 
#f0 and f1 the length of the sequence is n.
def fib(f0,f1,n):
    fib=[f0,f1]
    for i in range(n-2):
        fib.append(fib[-1]+fib[-2]) 
    return fib

#%%creating an example sequence
fib(1,2,12)
#%% Cassini's Identity
N=10
first=1
second=2

seq=fib(first,second,N+1)
for i in range(N):
    if (seq[i]**2)-(seq[i-1]*seq[i+1])==((-1)**(i-1)):
        print(i,'true')
    else:
        print(i,'false')


#%% Print out the last 10 terms of a sequence that you generated
print(fib(0,1,30)[-10:])

#last ten terms of the sequence starting with 0 and 1 going up to the 30th term.

