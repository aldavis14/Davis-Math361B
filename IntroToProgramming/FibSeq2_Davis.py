#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 20:38:19 2019

@author: allisondavis
"""

f0=0
f1=1
N=100
m=2
#%%

fib_seq=[f0,f1]
multiples=[]

for i in range(N-2):
    fib_seq.append(fib_seq[-1]+fib_seq[-2])
#print('Fibonacci Sequence:', fib_seq)
#%%
for ii in fib_seq:
    if ii%m==0:
        multiples.append(ii)
#print('Multiples of m:', multiples)
print('Number of terms divisible by m:', len(multiples))
#%%
percentage= len(multiples)/N
print(percentage*100)

#%%
#m=2, 33.3399999
#m=3, 25
#m=4, 16.6699999
#m=5, 20
#m=6, 8.34
#m=7, 12.5
#m=8, 16.6699999
#m=9, 8.34
#m=10, 6.67

#%%
for k in range(len(fib_seq)):
    if fib_seq[k]%m==0:
        print(k)

#Every third number in the sequence is even.

