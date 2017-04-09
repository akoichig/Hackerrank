#!/bin/python3
T = int(input().strip())
for case in range(T):
    N = int(input().strip())
    x, r3 = divmod(N, 3)
    y, r5 = divmod(N, 5)
    z, r15 = divmod(N, 15)    
    if r3==0:
        x -= 1
    if r5==0:
        y -= 1  
    if r15==0:
        z -= 1        
    ans = (3*x*(x+1)+5*y*(y+1)-15*z*(z+1)) // 2        
    print(int(ans))        
        
