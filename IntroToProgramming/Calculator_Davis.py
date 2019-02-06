#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 20:07:10 2019

@author: allisondavis
"""

#input variables

x=
y=
z=
#%%
#creating the list

calculator=[x+y,(y*z)+(3*x),(x+y)**2,(2*((y*z)+(3*x))-(0.5*x))/(x+y),7%3]
print(calculator)

calculator[2]=calculator[2]+3
print(calculator)

calculator[-1]=calculator[-1]*(3/4)
print(calculator)

print('The sum of the list is',sum(calculator))
