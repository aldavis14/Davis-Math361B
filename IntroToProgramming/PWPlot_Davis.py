#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 21:04:12 2019

@author: allisondavis
"""
import numpy as np
import matplotlib.pyplot as plt

N=40

x_values = np.linspace(-3, 3, N)


def f(x):
    y=[]
    for i in x:
        if (i<-2):
            y.append(-3*((i+2)**2)+1)
        elif (i>=-2 and i<-1):
            y.append(1)
        elif (i>=-1 and i<=1):
            y.append(((i-1)**3)+3)
        elif (i>1 and i<2):
            y.append(np.sin(i*np.pi)+3)
        else:
            y.append(3*np.sqrt(i-2)+4)
    plt.scatter(x_values,y)


f(x_values)
