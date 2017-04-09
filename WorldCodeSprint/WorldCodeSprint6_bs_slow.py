        

p = 'arelkjfdafd'

def pal(st):
    q, r = len(st) % 2
    b = [st[k]==st[-k-1] for k in range(2*q)]
    return len(b)==sum(b)
        
pals = []
for s in range(len(p)):
    for t in range(s,len(p)+1):
        sub = p[s:t]
        if pal(sub):
            pals.append(sub)
pals.sort()            

def f(p):
    for ch in p:
        ord(ch)

n =         2
