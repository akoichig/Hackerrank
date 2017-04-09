#!/bin/python3
# 10! is the first factorial greater than 10**6
# https://www.hackerrank.com/contests/projecteuler/challenges/euler020
# https://www.hackerrank.com/contests/projecteuler/challenges/filters/page:15

# Gather Data
LIMIT = 100000
d = [0]+[1]*(LIMIT-1)
for k in range(2,LIMIT):
    q, r = divmod(LIMIT, k)
    s = ([0]*(k-1)+[k])*q + [0]*r
    #d = [a+b for a, b in zip(d, s)]
    d = [d[i]+s[i] if i>k else d[i] for i in range(LIMIT)]
print(d[219], d[283])    

OldN = 1
NewN = 10000
amicable = []
maxb = 0
for i in range(OldN-1, NewN-1):
    b = d[i];
    if b == i+1 or i+1>b:
        continue
    if b>maxb:
        maxb = b
        print(i,maxb)
    if b-1>LIMIT: # compute d[b] directly 
        print(b-1, " is too big.")
    else:
        if d[b-1] == i+1:
            amicable.append(i+1)
            amicable.append(b)
print(amicable)

factorial_memo = {0: 1, 1:1}
def factorial(n):
    if n not in factorial_memo:
        factorial_memo[n] = n*factorial(n-1)
    return factorial_memo[n]


def main():
    T = int(input().strip())
    for _ in range(T):
        N = int(input().strip())
        f = factorial(N)
        print(sumDigits(str(f)))  

def main2():
    T = 1 # DEBUG
    for _ in range(T):
        N = 5 # DEBUG
        f = factorial(N)
        print(f)
        print(sumDigits(str(f)))  


