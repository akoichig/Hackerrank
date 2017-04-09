#!/bin/python3
# https://www.hackerrank.com/contests/projecteuler/challenges/euler016/submissions

# Original function using divmod
def sumDigitsOld(N):
    sum = 0
    while N != 0:
        q,r = divmod(N, 10)
        sum += r
        N = q
    return sum

# improved solution uses string
def sumDigits(N):
    sum = 0
    for s in N:
        sum += int(s)
    return sum

T = int(input().strip())
for _ in range(T):
    N = int(input().strip())
    print(sumDigits(str(2**N)))  

