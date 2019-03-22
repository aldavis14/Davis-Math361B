#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 15:54:24 2019

@author: allisondavis
"""
# a0 initial term in sequence
# N total number of terms to compute in sequence 

def collatz(a0, N):
    sequence = [a0]
    while len(sequence) < N:
        if sequence[-1] % 2 == 0:
            sequence.append(sequence[-1]/2)
        elif sequence[-1]==1:
            break
        else:
            sequence.append(3*sequence[-1]+1)
    if sequence[-1]==1:
        print('It takes '+str(len(sequence))+' terms to reach 1.')
    else:
        print('The sequence does not reach 1 in '+str(N)+' terms.')
    return(sequence)
        
#%% Try examples
collatz(6,5)

#%%
collatz(729, 110)


