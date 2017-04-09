#!/usr/bin/python
#!/bin/python3

def largestprime(num):
    maxi = -1
    temp = num
    p = 2
    while p**2<=temp:
        #print("START: p, num, temp = ", p, num, temp)
        while num % p ==0:
            if p > maxi:
                maxi = p
            num /= p
        p += 1
        #print("END: p, num, temp = ", p, num, temp)            
    if (num > 1 and num > maxi):
        maxi = num
    return int(maxi) 

def smallestprime(num):
	if num % 2 == 0: return 2
	p = 3
	while p**2<= num and num % p != 0:
		p+= 2
	if num % p == 0: 
		return p
	else:
		return num
    
t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    print(largestprime(n))
