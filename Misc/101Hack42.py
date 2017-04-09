#!/usr/bin/python
# 101 Hack 42 2016-10-18

# Debugging
# http://stackoverflow.com/questions/4929251/can-you-step-through-python-code-to-help-debug-issues
# https://pythonconquerstheuniverse.wordpress.com/2009/09/10/debugging-in-python/

#import pdb
#pdb.set_trace()



#n = int(input().strip())
#cases =[1, 150, 140, 2015, 3013, 4444, int(10**6)]
#cases = [int(c) for c in cases]
q=1 # number of queries
a, b = ['daBcd', 'ABC']

# Fibonacci memoization:
fib_memo = {}
ans_memo = {}

def fib(k):
    if k < 2: return k
    if k not in fib_memo:
        fib_memo[k] = fib(k-1)+fib(k-2)
    return fib_memo[k]
def ans(n):
    if n==1: return 0
    if n not in ans_memo:
        k=1
        while fib(k)<= n:
            k+= 1
        q = (k-1) // 3            
        ans_memo[n] = sum([fib(3*i) for i in range(q+1)])    
    return ans_memo[n]
    
# Generic main function
#t = int(input().strip())
#for a0 in range(t):
#    n = int(input().strip())
#    print(ans(n))
    

def main(a,b):
    if len(b)>len(a):
        print("NO")
    else:
        i=j=0
        while j<len(b) and i<len(a):
                if b[j]!=a[i] and b[j].lower()!=a[i]:
                    i+=1                
                else:
                    j+=1
                    i+=1
        if j==len(b):
            print("YES")
        else:
            print("NO")
main(a, b)            
    
def main2(n):
    # Retrieving previous data
    try:
        with open('primefile') as f:
            p = [int(prime.strip()) for prime in f]
        f.close()
        with open('afile') as f:
            a = [int(ans.strip()) for ans in f]
        f.close()
            
        #p = [int(ans.strip()) for ans in open('primefile')]
        #a = [int(ans.strip()) for ans in open('afile')]
    except OSError:
        p = [2]
        a = [0,0]
    except IOError:
        p = [2]
        a = [0,0]
    print('length of a = ', len(a))
    print('length of p = ', len(p))
    if n <= len(a): 
        print(a[n-1])
    else: 
        newk = len(a)+1
        while newk <= n:
            numprimes = 0
            for prime in p:
                curprime = prime
                if prime <= newk/2:
                    if (newk % prime)==0:
                        numprimes += 1
                else:
                    break
            if (numprimes==0) and (newk != curprime):        
                p.append(newk)
            a.append(a[newk-2]+int(numprimes*(numprimes-1)/2))
            newk += 1
        print(a[n-1])

    # Logging
    with open('primefile', "w") as f:
        for prime in p:
            f.write(str(prime)+'\n')
    f.close()            
    with open('afile', "w") as f:
        for ans in a:
            f.write(str(ans)+'\n')   
    f.close()
def testing():
    p=[]
    a=[]
    try:    
        p = [int(ans.strip()) for ans in open('primefile')]
        a = [int(ans.strip()) for ans in open('afile')]
    except OSError:
        p = 'test'
        a = 'test'
    except IOError:
        p = 'test2'
        a = 'test2'        
    print(p,a)

#for n in cases:
#    main(n)

    
