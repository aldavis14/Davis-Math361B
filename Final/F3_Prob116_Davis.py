#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  2 10:42:50 2019

@author: allisondavis
"""

# Define the number of tiles.
N = 8
r = 2
g = 3
b = 4

# Create the function. 
def one_color(color, N): 
    ways = [1] * color + [0] * (N-color+1) 
    
    for ii in range(color, N+1):
        ways[ii] += ways[ii - 1] + ways[ii - color]
    return ways[N] - 1

all_colors = one_color(r, N) + one_color(g, N) + one_color(b, N)

# Print Statement.
print ('The total number of ways to fill '+str(N)+' spaces with each color tile: '+str(all_colors))
