#!/bin/python3

# With N=5*10**6, the the maximum number is  1318802294932 (achieved by 4637979)
# Also, the maximum number of steps is 596, achieved by 3,732,423
import sys

def nextTerm(n):
    if n % 2 == 0:
        return int(n/2)
    else:
        return 3*n+1

len_memo = {1:0}

def f(n):

    if n not in len_memo:
        step = 0
        seq = [n]
        k = n
        while k != 1:
            k = nextTerm(k)
            seq.append(k)
            step += 1
        for k in seq:
            len_memo[k] = step
            step -= 1
    return len_memo[n]

def main():
    global indices
    global lengths
    #T = int(input().strip())
    T = 1
    indices = [1] # stores record-breaking n
    lengths = [0] # stores lengths of record-breaking n

    for _ in range(T):
        #N = int(input().strip())
        N = 50000
        print(ans(N))

def ans(N):
    # Check if new data is needed
    if indices[-1] >= N:
        # retrieve largest n<= N
        for i in range(len(indices)):
            if indices[i] > N:
                break
        if indices[i]==N:
            return N
        idx = i-1
        longest = lengths[idx]

        # Look for ties between idx and N
        k = N
        while k > idx:
            if f(k) == longest: return k
            k -= 1
        return idx

    idx = indices[-1]    
    longest = lengths[-1]
    for n in range(indices[-1], N+1):
        clen = f(n)
        if clen > longest:
            idx = n
            indices.append(n)
            lengths.append(clen)
            longest = clen
        elif clen == longest:
            idx = n
    return idx
            
        
        

def main2():
    #cases = [5000000]
    N = 50000
    
    cases = range(1,N)
    ans = 600
    maxnum = -1
    indices = []
    lengths = []
    for n in cases:
        clen = f(n)
        if clen<ans:
            indices.append(n)
            lengths.append(clen)
            print(n, "breaks new record:", clen)
            ans = clen
     
        

main2()
