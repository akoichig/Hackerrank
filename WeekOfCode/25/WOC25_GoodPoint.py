#!/bin/python3

from matplotlib import pyplot as plt
from shapely.geometry.polygon import LinearRing, Polygon
from random import Random
random = Random()

def polyplot(p):
    poly = Polygon([(x,y) for x,y in zip(p[::2], p[1::2])])
    x,y = poly.exterior.xy
    fig = plt.figure(1, figsize=(5,5), dpi=90)
    #fig.clf()
    ax = fig.add_subplot(111)
    ax.plot(x, y, color='#6699cc', alpha=0.7, linewidth=3, solid_capstyle='round', zorder=2)
    ax.set_title('Polygon')
    fig.show()


    
from math import sqrt
def polysort(p):   
    xlist = p[::2]
    ylist = p[1::2]
    ylist, xlist = (list(t) for t in zip(*sorted(zip(ylist, xlist))))
    if xlist[0]>xlist[1]:
        xlist[0], xlist[1] = xlist[1], xlist[0] 
        ylist[0], ylist[1] = ylist[1], ylist[0]
    if xlist[-2]>xlist[-1]:
        xlist[-2], xlist[-1] = xlist[-1], xlist[-2] 
        ylist[-2], ylist[-1] = ylist[-1], ylist[-2]
    xline = xlist[-1]
    xleft = [xlist[i] for i in range(len(xlist)) if xlist[i]<=xline]
    yleft = [ylist[i] for i in range(len(xlist)) if xlist[i]<=xline]
    xleft = xleft[::-1]
    yleft = yleft[::-1]
    xright = [xlist[i] for i in range(len(xlist)) if xlist[i]>xline]
    yright = [ylist[i] for i in range(len(xlist)) if xlist[i]>xline]
    xlist = xleft + xright
    ylist = yleft + yright
    p =[]
    for x,y in zip(xlist, ylist):
        p.extend([x,y])
    return p

def hyperplane(x1, y1, x2, y2, x3, y3, x, y):
    if x1 == x2:
        return (x<=x1)==(x3<=x1)
    elif x1 > x2:
        dx = x1-x2
        dy = y1-y2
    else:
        dx = x2-x1
        dy = y2-y1
    return (dx*y<=dx*y1+dy*(x-x1))==(dx*y3<=dx*y1+dy*(x3-x1))
    
def checkpoly(p, x, y):
    k = int(len(p)/2)
    for i in range(k):
        x1, y1 = p[(2*i)%k], p[(2*i+1)%k]
        x2, y2 = p[(2*i+2)%k], p[(2*i+3)%k]
        x3, y3 = p[(2*i+4)%k], p[(2*i+5)%k]
        if not hyperplane(x1, y1, x2, y2, x3, y3, x, y):
            return False
    return True        
        
def checkell(e, x, y):
    x1, y1, x2, y2, a = e
    return sqrt((x-x1)**2+(y-y1)**2)+sqrt((x-x2)**2+(y-y2)**2)<= 2*a

def score(x,y):
    val = 0
    for p in P:
        val += checkpoly(p, x, y)
    for e in E:
        val += checkell(e, x, y)
    return val

def findpt(L, D, R, U):
    k = 1
    while k<10:
        for i in range(k+1):
            for j in range(k+1):
                dx = (R-L)/float(k)
                dy = (U-D)/float(k)
                if score(L+i*dx, D+j*dy)==n+m:
                    print(" in score, k = ", k) # testing
                    return L+i*dx, D+j*dy
    
        k+=1 
    return (L+R)/float(2), (D+U)/float(2)

P = []
E = []
L = D = -10**4
R = U = 10**4
#n = int(input().strip())
n = random.randint(1,4) # testing
for _ in range(n):
    #v = int(input().strip())
    v = random.randint(3,10) # testing

    p = []
    pxmin = pymin = 10**4
    pxmax = pymax = -10**4
    for _ in range(v):
        #x, y = list(map(int, input().strip().split()))
        x = random.randint(-5,5) # testing
        y = random.randint(-5,5) # testing
        pxmin = min(x, pxmin)
        pxmax = max(x, pxmax)
        pymin = min(y, pymin)
        pymax = max(y, pymax)
        p.extend([x,y])
    p = polysort(p)
    polyplot(p)
    print("polygon: ",p)
    P.append(p)
    L = max(pxmin, L)
    R = min(pxmax, R)
    D = max(pymin, D) 
    U = min(pymax, U)
#m = int(input().strip())
m = random.randint(1,5) # testing

exmin = eymin = -10**4
exmax = eymax = 10**4
for _ in range(m):
    #x1, y1, x2, y2, a = list(map(int, input().strip().split()))
    x1 = random.randint(-5,5) # testing
    y1 = random.randint(-5,5) # testing
    x2 = random.randint(-5,5) # testing
    y2 = random.randint(-5,5) # testing
    
    dx = x2 - x1
    dy = y2 - y1
    h = (x1+x2)/float(2)
    k = (y1+y2)/float(2)
    if dx!=0 or dy!=0:
        
        f = sqrt(dx**2+dy**2)/float(2)
        a = random.randint(int(f)+1,10) # testing
        M = float(dx*dy)/(4*a*a-dx*dx)
        print("ellipse: ", x1, y1, x2, y2, a) # testing
        b = sqrt(a**2-f**2)
        G = (dx*dy*(2*a*a-f*f))/float(f*f*dy*dy+a*a*(dx*dx-dy*dy))
        # what if foci are same (circle?)
        c = float(dx)/sqrt(dx*dx+dy*dy)
        s = float(dy)/sqrt(dx*dx+dy*dy)
        exmin = max(h-a*b/sqrt(b*b*(c+G*s)**2+a*a*(s-G*c)**2), exmin)
        exmax = min(h+a*b/sqrt(b*b*(c+G*s)**2+a*a*(s-G*c)**2), exmax)
        eymin = max(k-a*b/sqrt(b*b*(M*c+s)**2+a*a*(M*s-c)**2), eymin)
        eymax = min(k+a*b/sqrt(b*b*(c+G*s)**2+a*a*(s-G*c)**2), eymax)
    else: #circle case
        exmin = max(x1-a, exmin)
        exmax = min(x1+a, exmax)
        eymin = max(y1-a, eymin)
        eymax = min(y1+a, eymax)                 
    E.append([x1, y1, x2, y2, a])
L = max(L, exmin) 
R = min(R, exmax)
D = max(D, eymin)
U = min(U, eymax)
x, y, = findpt(L, D, R, U)
print(x)
print(y)
