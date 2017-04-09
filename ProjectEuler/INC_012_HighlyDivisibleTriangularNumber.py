#!/bin/python3

# Find first triangular number having over N divisors (1<= N<= 1000)

def numDiv(n):
    limit = n
    num = 0
    if n == 1:
        return 1
    i = 1
    while i < limit:
        if n % i == 0:
            limit = n / i
            if limit != i:
                num += 1
            num += 1
        i += 1
    return num 

def ans(N):
    k = 1    
    T1 = k*(2*k-1)
    T2 = k*(2*k+1)
    n1 = numDiv(k)
    n2 = numDiv(2*k-1)
    n3 = numDiv(2*k+1)
    while n1*n2<=N and n1*n3<=N:
        k += 1
        T1 = k*(2*k-1)
        T2 = k*(2*k+1)
        n1 = numDiv(k)
        n2 = numDiv(2*k-1)
        n3 = numDiv(2*k+1)
    if n1*n2>N:
        return T1
    else:
        return T2
        
T = int(input().strip())
for _ in range(T):
    N = int(input().strip())
    print(ans(N))
