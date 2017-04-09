
a='aBccCdD'; b='ABCCC'
alow = a.lower()
blow = b.lower()

if len(a)<len(b):
    print("NO")
    #continue
posa = 0
posb = 0
found = 0
flag=0
#print(s1, s2, len(s1), len(s2))
# Build list returning caps[pos_in_A]=cap_in_A
caps = [0]*len(a)
acapkeys = []
for i in range(len(a)):
    if a[i]!=alow[i]:
        caps[i]=a[i]
        acapkeys.append(i)
        
for capi in acapkeys:
#for capi in [5]:
    if posb!=len(b):
        cap = a[capi]
        ## find cap in b.
        ## if found at posb, then we can ignore lower case letters in a before capi
        ## if found > posb, then match a lowercase substring
        try:
            capb = b[posb:len(b)].index(cap)+posb
        except ValueError:
            #print("NO")
            flag = 1
            break
            #continue? break? set flag?
        if capb==posb:
            posa = capi+1 # or capa+1?
            posb = capb+1 # or capb+1?
        else:
            try:
                a[posa:capi].index(blow[posb:capb])
                posa = capi+1
                posb = capb+1
            except ValueError:
                #print("NO")
                flag=1
                break
                #continue? break? set flag?
    else:
        break
## No more caps in a
if flag:
    print("NO")
elif posb==len(b):
    print("YES")
else:
    try:
        a[posa:len(a)].index(blow[posb:len(b)])
        print("YES")
    except ValueError:
        print("NO")
        
