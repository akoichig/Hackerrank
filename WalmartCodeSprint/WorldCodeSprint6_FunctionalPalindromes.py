#n, k = input().strip().split()
#n, k = [int(n), int(k)]
n, k = [5, 2]
H = [[6, 7], [-1, 1], [0, 1], [2, 5], [3, 7]]
#H=[]
#for hd in range(n):
#    h1, h2 = input().strip().split()
#    h1, h2 = [int(h1), int(h2)]
#    H.append([min(h1, h2), max(h1, h2)])

# SHIFT DATA RIGHT
left = min([hd[0] for hd in H])
right = max([hd[1] for hd in H])
## shift right
H = [[hd[0]-left, hd[1]-left] for hd in H]
#print(H)

right = right-left
left = 0
#print(right)

#Hcenter = [(hpair[0]+hpair[1])/2 for hpair in H]
Hcenter=[]
for hpair in H:
    ctr = (hpair[0]+hpair[1])/2
    w = abs(hpair[0]-ctr)+abs(hpair[1]-ctr)
    Hcenter.append([ctr, w])
print(Hcenter)

nline = [0]*(1+right-left)
for i in range(len(nline)):
    for hd in H:
        nline[i]+=int(hd[0]<=i<=hd[1])

newnline = [0]*(1+right-left)        
for j in range(5):
    for i in range(len(nline)):
        rad = 1
        nbs = 1+min(len(nline)-1, i+rad)-max(0,i-rad)
        newv = float(sum(nline[max(0,i-rad):min(len(nline)-1,i+rad)]))/nbs
        newnline[i]=newv
        #print(newnline[:])
#print(nline)
        

def D(c, h1, h2):
    if c<left or c>right:
        return 2*(right-left)
    else:
        return (c<h1)*(h1-c) + (c>h2)*(c-h2)

## Initialize
spacing = (right-left)/(k-1)
#X=[0]*(right-left)
#locs = [cp*spacing for cp in range(k)]
locs = [i[0] for i in sorted(enumerate(newnline), key=lambda x:x[1], reverse=1)][0:k]
print(locs)
#locs = [1, 6]

## Hook up HDDs
mp = [0]*len(H)
for hdi in range(len(H)):
    cost = (right-left)*2
    hd = H[hdi]
    for l in locs:
        lcost = D(l, hd[0], hd[1])
        lcostL = D(l-1, hd[0], hd[1])
        lcostR = D(l+1, hd[0], hd[1])
        if lcost<cost:
            mp[hdi]=[l, lcost, lcostL, lcostR]
            cost = lcost
            
totCost = sum([hd[1] for hd in mp])            

# for l in locs
for itr in range(100):
    for l in locs:
        M = sum([hd[1] for hd in mp if hd[0]==l])
        L = sum([hd[2] for hd in mp if hd[0]==l])
        R = sum([hd[3] for hd in mp if hd[0]==l])
        if L<M and L<R:
            for i in [i for i in range(n) if mp[i][0]==l]:
                mp[i] = [l-1, mp[i][2], D(l-2,H[i][0], H[i][1]), mp[i][1]]
        if R<M and R<L:
            for i in [i for i in range(n) if mp[i][0]==l]:
                mp[i] = [l+1, mp[i][3], mp[i][1], D(l+2,H[i][0], H[i][1])]
        totCost = sum([hd[1] for hd in mp])
        #print(totCost)

finCost = 2*totCost + sum([hd[1]-hd[0] for hd in H])
print(int(finCost))


    
