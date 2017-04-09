#!/usr/bin/python
def check(r):
    #print("r = ", r)
    if r<101101 or r>=n: return False
    x = str(r)
    return x==x[::-1]         

def ans(n): 
    K = 999 #int(n/100)+1
    #print("K = ", K)    
    temp = -1
    for A in list(reversed(range(100,K+1))):
        for B in list(reversed(range(100,A+1))):
            if temp>A*B: break                
            if check(A*B):
                temp = A*B
                break
    return temp                
                        
       
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(ans(n))    
    
