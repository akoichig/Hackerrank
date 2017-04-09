#!/bin/python3

import sys
from operator import mul
from functools import reduce

t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    num = input().strip()
    maxprod = 0
    for i in range(n-k+1):
        x = map(int, [d for d in num[i:i+k]])
        p = reduce(mul, x, 1)
        if p > maxprod: maxprod = p
    print(maxprod)            

