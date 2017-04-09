#!/bin/python3

import sys

   
def highestPow(arr, p):
    k = 0
    A = [x for x in arr if x%p!=0]
    B = [x for x in arr if x%p==0]
    while B != []: # there is still a multiple of p
        B = [x/p for x in B if (x/p)%p==0]
        A.extend([x/p for x in B if (x/p)%p != 0])
        k+=1
    return A, k     

# get prime list up to 40
primes = list(map(int, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]))
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    arr = list(range(1,n+1))
    ans = 1
    primesn = [p for p in primes if p<=n]
    for p in primesn:
        arr, k = highestPow(arr, p)
        ans *= p**k
    print(ans)     

# ALTERNATIVE APPROACHES:
from functools import reduce
def gcd(a, b): return a if b == 0 else gcd(b,a%b)
def lcm(a, b): return a / gcd(a, b) * b
t = int(raw_input())
for tc in xrange(t):
    N = int(raw_input())
    print reduce(lambda a, b: lcm(a, b), range(1, N+1))   
    

