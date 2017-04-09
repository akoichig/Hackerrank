#!/bin/python3

# NOT PASSING LAST TEST CASE
# IMPLEMENT SIEVE OF ERATOSTHENES

import sys

def isPrime(p):
    # assume list primes is populated up to sqrt(n). If not, we should check all odds.
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

# sum prime memoization:
sumPrime_memo = {'1': 0, '2': 2}

def sumPrime(n):
    if n not in sumPrime_memo:
        keys = sumPrime_memo.keys()
        if keys:
            m = max([int(k) for k in keys if int(k)<= n])
            #print("m , n = ", m, n)
            #print(sumPrime_memo[str(m)])
            sumPrime_memo[str(n)] = sumPrime_memo[str(m)]+sum([p for p in primes if m<p<=n])       
    return sumPrime_memo[str(n)]       

        
primes = [2,3,5,7,11,13,17,19,23,29]
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    
    # POPULATE PRIME LIST PAST N
    while primes[-1]<n:
        getNextPrime() 
    print(sumPrime(n))



# BEST ATTEMPT (PASSES ALL TEST CASES EXCEPT LAST ONE - TIMES OUT)
#!/bin/python3
import sys    
import functools
@functools.lru_cache(maxsize=None) 
def primes_sieve(limit):
    a = [True] * (limit+1)
    a[0] = a[1] = False
    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit+1, i):
                a[n] = False
    return a                
        
#primes = [2,3,5,7,11,13,17,19,23,29]
primes = primes_sieve(10**6)
primes = list(primes)
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    
    # POPULATE PRIME LIST PAST N
    #while primes[-1]<n:
    #    getNextPrime() 
    #print(sumPrime(n))
    print(sum([p for p in primes if p<=n]))  


