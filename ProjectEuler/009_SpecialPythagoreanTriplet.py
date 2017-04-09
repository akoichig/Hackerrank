#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    ans = -1
    prev = -2
    for a in range(1,int(n/2)):
        b1 = n*(n-2*a) 
        b2 = 2*(n-a)
        if b1 % b2 == 0:
            if a*b1*(n*b2-a*b2-b1) >= ans*b2*b2:
                ans = a*(b1/b2)*(n-a-b1/b2)
            
    print(int(ans))                

