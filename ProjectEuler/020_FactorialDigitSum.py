#!/bin/python3
# https://www.hackerrank.com/contests/projecteuler/challenges/euler020
# https://www.hackerrank.com/contests/projecteuler/challenges/filters/page:15


factorial_memo = {0: 1, 1:1}
def factorial(n):
    if n not in factorial_memo:
        factorial_memo[n] = n*factorial(n-1)
    return factorial_memo[n]


def sumDigits(N):
    sum = 0
    for s in N:
        sum += int(s)
    return sum

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

