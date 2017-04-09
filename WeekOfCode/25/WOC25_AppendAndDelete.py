#!/bin/python3

import sys


s = input().strip()
t = input().strip()
k = int(input().strip())

def ans(s, t, k):   
    # Count the beginning letters in common
    m = min(len(s),len(t))
    try:
        i = [s[i]== t[i] for i in range(m)].index(False)
    except:
        if len(s)==len(t):
            if k%2==0 or 2*m<=k: 
                return "Yes"
            else:
                return "No"
        i = len(s)            
    # Delete additional letters in s, if needed
    numToDelete = len(s)-i
    if numToDelete > k:
        return "No"
    #s = s[:i]
    k -= numToDelete

    #print(i, numToDelete, numToAppend)

    # Append letters to s, if needed
    numToAppend = len(t)-i
    if numToAppend > k:
        return "No"
    k -= numToAppend
    if k % 2 == 0:
        return "Yes"
    else:
        return "No"
    
print(ans(s,t,k))
    
