#!/bin/python3

# memoize

import sys

fib_memo = {}
ans_memo = {}

def fib(k):
    if k < 2: return k
    if k not in fib_memo:
        fib_memo[k] = fib(k-1)+fib(k-2)
    return fib_memo[k]
def ans(n):
    if n==1: return 0
    if n not in ans_memo:
        k=1
        while fib(k)<= n:
            k+= 1
        q = (k-1) // 3            
        ans_memo[n] = sum([fib(3*i) for i in range(q+1)])    
    return ans_memo[n]
    
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(ans(n))
    #print(fib_memo)
    #print(ans_memo)
