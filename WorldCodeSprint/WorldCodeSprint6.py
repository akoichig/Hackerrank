def comm():
    n=3
    for d in range(n):
        print("\td = {}".format(d))
        for x in range(1+int((n-d)/2)):
            y = x+d
            z = n-y-x
            print("{} {} {}".format(x, y, z))

N=1
T = [['x'], ['x', 1]]
loc = [[1,1]]

def L(d):
    T = d[0]
    loc = d[1]
    new = [[0]]
    newloc = []
    for i in range(len(T)):
        new.append([0]+T[i])
    for i in range(len(loc)):
        lx = loc[i][0]
        ly = loc[i][1]
        new[lx-ly][0]='x'
        new[lx+1][0]='x'
        newloc.append([lx+1, ly+1])
        nl = sum([1 for t in new if t[0]==0])
    return new, newloc #, nl

def D(d):
    T = d[0]
    loc = d[1]
    new = T + [[0]*(len(T)+1)]
    for i in range(len(loc)):
        lx = loc[i][0]
        ly = loc[i][1]
        new[len(T)][len(T)-lx+ly]='x'
        new[len(T)][ly]='x'
        nl = sum([1 for t in new[len(T)] if t==0])
    return new, loc #, nl

def U(d):
    T = d[0]
    loc = d[1]
    new = [[0]]
    newloc = []
    for i in range(len(T)):
        new.append(T[i]+[0])
    for i in range(len(loc)):
        lx = loc[i][0]
        ly = loc[i][1]
        new[lx+1][lx+1]='x'
        new[ly][ly]='x'
        newloc.append([lx+1, ly])
        nl = sum([1 for i in range(len(new)) if new[i][i]==0])
    return new, newloc #, nl

def fill(d):
    T = d[0]
    loc = d[1]
    i=0
    for i in range(len(T)):
        for j in range(len(T[i])):
            if T[i][j] == 0:
                break
        else:
            continue
        break    
    T[i][j] = 1
    loc.append([i, j])
    return T, loc

def pr(d):
    print('\n')
    T = d[0]
    for i in T:
        sti = [str(j) for j in i]
        print('  '.join(sti))

N = 10
def init(T, N):
    T = []
    for r in range(N):
        T.append([0]*(r+1))
    return T
        



def fill2(T, r, c):
    l = T[:]
    l[r][c]=1
    for i in range(c,r):
        l[i][c]='x'
    for i in range(r+1,len(T)):
        l[i][c]='x'
    for j in range(0,c):
        l[r][j]='x'
        l[j+(r-c)][j]='x'
    for j in range(c+1,r+1):
        l[r][j]='x'
    for k in range(c+1,len(T)-r+c):
        l[k+(r-c)][k]='x'
    return l

T = init(T, N)
fill2(T,2,2)
pr([T])
