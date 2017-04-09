#!/bin/python3

# In the 20x20 grid of numbers, find largest product of 4 adjecent numbers (horizontal, vertical, diagonal, antidigonal) 

import sys
def maxprod(a,i,j):
    if i<17 and j<17:
        x = y = z = a[i][j]
        w = a[i+3][j]
        for k in range(1,4):
            x *= a[i][j+k]
            y *= a[i+k][j]
            z *= a[i+k][j+k]
            w *= a[i+3-k][j+k]
        return max([x,y,z,w])            
    elif i>=17 and j<17:
        x = a[i][j]
        for k in range(1,4):
            x *= a[i][j+k]
        return x
    elif j<17 and i>=17:
        y = a[i][j]
        for k in range(1,4):
            y *= a[i+k][j]
        return y          
    else:
        return 0
                
