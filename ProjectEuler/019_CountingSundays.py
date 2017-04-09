#!/bin/python3
# 688 Sundays every 400 years    
# https://www.hackerrank.com/contests/projecteuler/challenges/filters/page:15

def test():
    with open('tests/019_test.txt') as f:
        content = f.readlines()
        content = [x.strip('\n').split() for x in content]
        return content
    f.close()

    
def main():
    T = int(input().strip())
    for _ in range(T):
        Date1 = list(map(int, input().strip().split()))
        Date2 = list(map(int, input().strip().split()))
        print(ans(Date1, Date2))

def isLeap(Y):
    if Y % 400 == 0:
        return True
    elif Y % 100 == 0:
        return False
    elif Y % 4 == 0:
        return True
    else:
        return False
    
def ans(Date1, Date2):
    Y1, M1, D1 = Date1
    Y2, M2, D2 = Date2
    #print(Date1, Date2)
    
    # Shift years to same 400 year cycle as 1900
    q,r = divmod(Y1 - 1900, 400)
    Y1, Y2 = Y1- q*400, Y2-q*400
    q,r = divmod(Y2-Y1, 400)
    Y2 -= q*400
    numSun = q*688

    Y = M = d = tempd = '__' # DEBUG
    debugprint(Y1, M1, D1, Y2, M2, D2, Y, M, numSun, d, tempd)
    
    # Determine day of week for Jan 1 Y1
    Y = 1900
    d = 1
    while Y != Y1:
        d = (d + 1 + isLeap(Y)) % 7
        Y += 1

    debugprint(Y1, M1, D1, Y2, M2, D2, Y, M, numSun, d, tempd)
    # If Y1==Y2, add sundays from M1 to M2
    if Y1 == Y2:
        M = M1-1
        tempd = d
        if M1 == M2 and D1>1:
            return numSun
        
        while M != M2-1:
            if tempd == 0:
                numSun += 1
            if isLeap(Y):
                tempd = (tempd + leapDays[M]) % 7
            else:
                tempd = (tempd + noleapDays[M]) % 7
            M += 1
        if tempd == 0 and D2 >= 1:
            numSun += 1
        return numSun
        
    # If Y1 < Y2, add Sundays for years Y1 to Y2-1
    # Compute numSun between Y1 an Y2
    print("NOW: Compute numSun between Y1 an Y2") # debug
            
    while Y != Y2:
        if isLeap(Y):
            numSun += leapDist[-d%7]
        else:
            numSun += noleapDist[-d%7]
        d = (d + 1 + isLeap(Y)) % 7
        Y += 1
            
    # Add Sun in Y2 up to M2 D2
    print("NOW: Add Sun in Y2 up to M2 D2")
    M = 0
    tempd = d
    while M != M2-1:
        debugprint(Y1, M1, D1, Y2, M2, D2, Y, M, numSun, d, tempd)        
        if tempd == 0:
            numSun += 1
        if isLeap(Y):
            tempd = (tempd + leapDays[M]) % 7
        else:
            tempd = (tempd + noleapDays[M]) % 7
        M += 1
    if tempd==0 and D2 >= 1:
        numSun += 1
    return numSun
    
    

def main3():
    global noleapDist
    global leapDist
    global noleapDays
    global leapDays
    day = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    noleapDist = [2, 1, 1, 3, 1, 2, 2]
    leapDist = [3, 1, 1, 2, 2, 1, 2]
    noleapDays = [3,0,3,2,3,2,3,3,2,3,2,3]
    leapDays = [3,1,3,2,3,2,3,3,2,3,2,3]

    # Get test data
    #content = test()
    content = testdata()
    print(content)
    T = int(content[0][0])
    for i in range(T):
        date1 = list(map(int, content[2*i+1]))
        date2 = list(map(int, content[2*i+2]))
        print(ans(date1, date2))
def debugprint(Y1, M1, D1, Y2, M2, D2, Y, M, numSun, d, tempd):
        print("  DEBUG: date1={} {} {} date2={} {} {} Y={} M={} numSun={} d={} tempd={}".format(Y1, M1, D1, Y2, M2, D2, Y, M, str(numSun).zfill(3), d, tempd))
        
def testdata():
    return [['1'] ,['1900', '5', '1'], ['1900', '7', '5']]

def scrap():    
    
    global noleapDist
    global leapDist
    global noleapDays
    global leapDays
    day = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
    noleapDist = [2, 1, 1, 3, 1, 2, 2]
    leapDist = [3, 1, 1, 2, 2, 1, 2]
    noleapDays = [3,0,3,2,3,2,3,3,2,3,2,3]
    leapDays = [3,1,3,2,3,2,3,3,2,3,2,3]
    
    Y = 1900
    d = 1
    sd = -d%7
    numSunYr = numSun = noleapDist[-d%7]
    print(numSunYr)
    for i in range(402):

        d = (d + 1 + isLeap(Y)) % 7
        Y += 1
        if isLeap(Y):
            numSunYr = leapDist[-d%7]
            numSun += numSunYr
        else:
            numSunYr = noleapDist[-d%7]
            numSun += numSunYr
        #if (Y-1900) % 100 == 0:
        print(Y, day[d], numSunYr, numSun)

main3()
#scrap()
