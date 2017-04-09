#!/bin/python3

# Work out the first ten digits of the sum of N 50-digit numbers.
N = int(input().strip())
x = []
s = []
for _ in range(N):
    x.append(input().strip())
place = 0
digitsum = 0
while place < 50:
    entry = -1-place
    digitsum += sum([int(d[entry]) for d in x])
    s.append(digitsum % 10)
    digitsum = int(digitsum/10)
    place += 1
#print(s)
#print(digitsum)
l = 10-len(str(digitsum))
ans = digitsum*10**l
i = 1
while i<=l:
    ans += s[-i]*10**(l-i)
    i+= 1
print(ans)

