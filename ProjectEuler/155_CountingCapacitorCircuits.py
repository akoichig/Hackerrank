#!/bin/python3
# Counting Capacitor Circuits
# https://www.hackerrank.com/contests/projecteuler/challenges/euler155
# https://www.hackerrank.com/contests/projecteuler/challenges/filters/page:15
# https://learnpythonthehardway.org/book/ex40.html

#!/bin/python3

import sys

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

def parallel(n1, d1, n2, d2):
    tempN = n1*d2+n2*d1
    tempD = d1*d2
    g = gcd(tempN, tempD)
    return (int(tempN/g), int(tempD/g))

def series(n1, d1, n2, d2):
    tempN = n1*n2
    tempD = n1*d2+n2*d1
    g = gcd(tempN, tempD)
    return (int(tempN/g), int(tempD/g))

def countCaps():
    cnt = 0
    distinctCaps = []
    for c in caps:
        for x in c:
            if x not in distinctCaps:
                cnt +=1
                distinctCaps.append(x)
    return cnt


n = int(input().strip())
caps = [[],[(1, 1)]]

l = 1 # lengths of capacitors

while l<=n:
    for i in range(1,1+len(caps)):
        if l<(i+i)<=n:
            j = i
            capsi = caps[i]
            if len(caps)-1<(i+j):
                newcaps = []
                for p in range(len(capsi)):
                    for q in range(p, len(capsi)):
                        x = capsi[p]
                        y = capsi[q]
                        newp = parallel(x[0], x[1], y[0], y[1])
                        news = series(x[0], x[1], y[0], y[1])
                        if newp not in newcaps:
                            newcaps.append(newp)
                        if news not in newcaps:
                            newcaps.append(news)
                caps.append(newcaps)
            else:
                for p in range(len(capsi)):
                    for q in range(p, len(capsi)):
                        x = capsi[p]
                        y = capsi[q]
                        newp = parallel(x[0], x[1], y[0], y[1])
                        news = series(x[0], x[1], y[0], y[1])
                        if newp not in caps[i+j]:
                            caps[i+j].append(newp)
                        if news not in caps[i+j]:
                            caps[i+j].append(news)                                          
        for j in range(max(l+1-i,i+1), min(len(caps),n+1-i)):
            capsi = caps[i]
            capsj = caps[j]
            if len(caps)-1<(i+j):
                newcaps = []
                for x in capsi:
                    for y in capsj:
                        newp = parallel(x[0], x[1], y[0], y[1])
                        news = series(x[0], x[1], y[0], y[1])
                        if newp not in newcaps:
                            newcaps.append(newp)
                        if news not in newcaps:
                            newcaps.append(news)
                caps.append(newcaps) 
            else:
                for x in capsi:
                    for y in capsj:
                        newp = parallel(x[0], x[1], y[0], y[1])
                        news = series(x[0], x[1], y[0], y[1])
                        if newp not in caps[i+j]:
                            caps[i+j].append(newp)
                        if news not in caps[i+j]:
                            caps[i+j].append(news)
                                
    l+=1            
    #print(caps)

print(countCaps())   


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

    
main2()

