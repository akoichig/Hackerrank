#!/usr/bin/python
import math

# Read data file

name = []
owned = []
allprices = []

with open('sample.txt') as f:
    for i in xrange(5):
        f.next()
    for line in f:
        line = line.strip().split()
        name.append(line[0])
        owned.append(0)
        allprices.append([float(p) for p in line[1:len(line)]])
f.close()        

m = 100.00
k = len(name)
d = len(allprices[0])
#m, k, d = input().strip().split()
#m, k, d = [float(m), int(k), int(d)]

money = m

# name = []
# owned = []

prices = []

#for stock in range(k):
#    stockdata = input().strip().split()
#    name.append(stockdata[0])
#    owned.append(int(stockdata[1]))
#    prices.append( [float(p) for p in stockdata[2:7]]) 

def printTransactions(money, k, d, name, owned, prices):
    txns = 0
    txnlist = []
    weight = 0.9  # lambda weight for weighted moving average btwn 0 and 1, should tune using cv
    if d>0:  # buy or sell
        ## Processing step
        mvavg=[]
        for stock in range(k):
            p = prices[stock]
            avg = sum([p[i]*(weight**(3-i)) for i in range(4)])/sum([weight**(3-i) for i in range(4)])
            mvavg.append( avg )
        ## sort stocks by p[4]-mvavg
        stocklist = sorted(range(k), key=lambda i: ((prices[i][4]-mvavg[i])/mvavg[i]))
        for stock in stocklist: # instead of range(k):
            p = prices[stock]    
            deviance = (p[4]-mvavg[stock])/mvavg[stock]
            if money>0 and deviance<0:
                shares = money // p[4]
                if shares > 0:
                    txns += 1
                    txnlist.append('{} BUY {:g}'.format(name[stock], shares))
                    money -= shares*p[4]
            elif money>0 and deviance>0 and owned[stock]>0:
                txns += 1
                txnlist.append('{} SELL {:g}'.format(name[stock], owned[stock]))
                #money += owned[stock]*p[4]
    if d==0:
        for stock in range(k):
            if owned[stock]>0:
                txns += 1
                txnlist.append('{} SELL {:g}'.format(name[stock], owned[stock]))
    print(txns)
    for txn in txnlist:
        print(txn)
    return txnlist

def update(money, name, owned, prices, txnlist):
    for txn in txnlist:
        if txn != 0: 
            print(txn)
            stock, action, shares = txn.split()
            i = name.index(stock)
            print(prices[i])
            if action == 'BUY':
                try:
                    owned[i] += int(shares)
                except IndexError:
                    print("ERROR HERE: i={}, owned[i]={}".format(i,owned[i]))
                money -= int(shares)*(prices[i][4])
            else:
                try:
                    owned[i] -= int(shares)
                except IndexError:
                    print("ERROR HERE: i={}, owned[i]={}".format(i,owned[i]))
                money += int(shares)*(prices[i][4])
    return money, owned



# debug
totaldays = 3
d=totaldays+5  # d >= 5
for day in range(4,d):  # current day is actually day+5
    print("\nROUND {}: ".format(day-4+1))
    prices = [allprices[i][day-4:day+1] for i in range(k)];
    #debug print("prices: {}".format(prices))
    txnlist = printTransactions(money, k, d-day-1, name, owned, prices)
    print("TRANSACTIONS: {}".format(txnlist))
    money, owned = update(money, name, owned, prices, txnlist)
    print("MONEY: {}\nOWNED: {}".format(money, owned))

    

# Log:
# Exploratory attempts:
# attempt 1: 47.02 for blindly buying if p[4]<p[3] and selling if p[4]>p[3]
# attempt 2: 12.05 for blindly buying if p[4]>p[3] and selling if p[4]<p[3]  
# Real attempts:
# attempt 3: 63.46 for buy if curprice < moving avg; sell if curprice>mvavg (doesn't watch out for tanking stocks)
# attempt 4: -62.45 sort by (p[4]-mvavg[i])/mvavg[i] to avoid influences from different price scales.
# attempt 5: -61.66 use weighted moving avg
# attempt 6: -63.89 use weighted moving avg with deviance thresholds to avoid tanking stocks
# attempt 7: -63.89 tweak thresholds

print("SCORE: {:.2f}".format(5*math.log(money)))



# https://www.analyticsvidhya.com/blog/2016/02/time-series-forecasting-codes-python/
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
%matplotlib inline
from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 15, 6

data = pd.read_csv('sample.txt', sep=" ", header = None, skiprows = 5)
print data.head
print '\n Data Types:'
print data.dtypes

data.index

data = data.transpose()
print data.head

ts = data[0]
ts = ts[1:len(ts)]
len(ts)
ts.head(10)
plt.plot(ts)
