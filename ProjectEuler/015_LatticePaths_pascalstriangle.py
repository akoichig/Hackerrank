#!/bin/python3
LIM = 10**9+7
import math
pascal = []
for i in range(1002):
    row = [1]*(i+1)
    pascal.append(row)
    for j in range(1,i):
        pascal[i][j] = (pascal[i-1][j-1]+pascal[i-1][j]) % LIM
        

T = int(input().strip())
for _ in range(T):
    N, M = input().strip().split()
    N, M = [int(N), int(M)]  
    print(pascal[N+M][N] % LIM)
