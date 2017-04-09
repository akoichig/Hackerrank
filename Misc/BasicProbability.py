from fractions import Fraction
from math import factorial
x=[5,4] # white/black balls
y=[7,6]

# Draw 1 to put into bag Y
# white -> Y
p1 = Fraction(x[0], sum(x))*Fraction(y[1],sum(y)+1)

# black -> Y
p2 = Fraction(x[1], sum(x))*Fraction(y[1]+1,sum(y)+1)
print(p1+p2)

# Day 3: Basic Probability Puzzles 7
pA=500; dA=Fraction(5,1000)
pB=1000; dB=Fraction(8,1000)
pC=2000; dC=Fraction(1,100)

# Number of defective  from A
num=pA*dA

# Number of defective total
den=pA*dA+pB*dB+pC*dC
print(Fraction(num,den))

# 500*.005/(500*.005+1000*.008+2000*.01)
# P(A | defective) = P(A & Defective) / P(Defective) =


# Day 3: Basic Probability Puzzles 8
nmorn = Fraction(1,2)
neve = Fraction(2,5)
both = Fraction(1,5)
print((1-nmorn)+(1-neve)-both)

# Day 3: Basic Probability Puzzles 9
A = 12
B = 15
C = 10
# Find 1 - P(not selected)
print(1-Fraction(A-1,A)*Fraction(B-1,B)*Fraction(C-1,C))

# Day 3: Basic Probability Puzzles 10
B = Fraction(1,3)
N = Fraction(1,5)
# P(only B) + P(only N)
print(B*(1-N)+N*(1-B))
