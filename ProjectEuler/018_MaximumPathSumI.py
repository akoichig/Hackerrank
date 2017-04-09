#!/bin/python3

def next(indices, allSums, row):
    j = len(row)-1
    newIndices = []
    newSums = []
    for k in range(len(indices)):
        i = indices[k]
        x = allSums[k]
        if 0<= i-1:
            newIndices.append(i-1)
            newSums.append(x+row[i-1])
        if i<= j:
            newIndices.append(i)
            newSums.append(x+row[i])
    return newIndices, newSums

def ans(triangle):
    indices = range(len(triangle))
    allSums = triangle[-1]
    for row in triangle[::-1][1:]:
        indices, allSums = next(indices, allSums, row)
        #print(allSums)
    return max(allSums)

def main():
    T = int(input().strip())
    for _ in range(T):
        triangle = []
        N = int(input().strip())
        for _ in range(N):
            row = list(map(int, input().strip().split()))
            triangle.append(row)
        print(ans(triangle))
main()

# BELOW ARE OLD (WRONG) ATTEMPTS
def nextSum(oldSum, arr):
    enlargedSum = [oldSum[0]] + [x for x in oldSum[1:-1] for _ in (0,1)] + [oldSum[-1]]
    doubledSum = [x for x in arr for _ in range(2**())]
    return [a+b for a,b in zip(doubledSum, arr2)]

def nextSum(oldSum, arr):
    arr2 = [arr[0]] + [x for x in arr[1:-1] for _ in (0,1)] + [arr[-1]]
    doubledSum = [x for x in oldSum for _ in (0,1)]
    return [a+b for a,b in zip(doubledSum, arr2)]

    
        
def test():
    with open('tests/018_test.txt') as f:
        content = f.readlines()
        content = [x.strip('\n').split() for x in content]
        return content
    f.close()

def ans(triangle):
    indices = range(len(triangle))
    allSums = [0]
    for row in triangle:
        allSums = nextSum(allSums, row)
    return max(allSums)


def main3():
    content = test()
    triangle = []
    for j in range(2,len(content)):
        triangle.append(map(int, content[j]))
    print(triangle)
    print(ans2(triangle))
    
def main2():
    content = test()
    triangle = []
    for j in range(2,len(content)):
        triangle.append(map(int, content[j]))
    print(triangle)
    print(ans(triangle))

        
