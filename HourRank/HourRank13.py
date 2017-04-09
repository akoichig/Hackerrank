
#!/usr/bin/python

# Debugging
# http://stackoverflow.com/questions/4929251/can-you-step-through-python-code-to-help-debug-issues
# https://pythonconquerstheuniverse.wordpress.com/2009/09/10/debugging-in-python/

#import pdb
#pdb.set_trace()



#n = int(input().strip())
cases =[1, 150, 140, 2015, 3013, 4444, int(10**6)]
cases = [int(c) for c in cases]
def main(n):
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

for n in cases:
    main(n)

    
