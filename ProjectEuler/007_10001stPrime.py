#!/bin/python3

import sys

def isPrime(p):
    i = 0
    q=primes[0]
    while q**2 <= p:
        if p % q == 0:
            return False
        i += 1
        q = primes[i]
    return True        

def getNextPrime():
    p = primes[-1]+2
    while not isPrime(p):
        p += 2
    primes.append(p)        
        
primes = [2,3,5,7,11,13,17,19,23,29]
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    if n<=len(primes):
        print(primes[n-1])
    else:
        k = n-len(primes)
        while k>0:
            getNextPrime()
            k -= 1
        print(primes[-1])
        
