#!/bin/python3

single = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
teens = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
double = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
groups = ['Billion', 'Million', 'Thousand', '']

def trimleft(word):
    if word=='':
        return word
    if word[0]==' ':
        word = word[1:]
    return word

def trimright(word):
    if word=='':
        return word
    if word[-1]==' ':
        word = word[:len(word)-1]
    return word

def concat(left,right): # fixes spacing, perhaps overkill but simple
    return trimright(left)+' '+trimleft(right)
        
def constructTwo(part):
    if part == '00':
        numWord = ''
    elif part[0] == '0':       
        numWord = single[int(part[1])]
    elif part[0] == '1':
        numWord =  teens[int(part[1])] 
    else:
        numWord = double[int(part[0])]
        if part[1] != '0':
            numWord = concat(numWord, single[int(part[1])])
    return numWord
    
def constructThree(part, i):
    numWord = ''
    if part == '000':
        return numWord
    if part[0] != '0':
        numWord = concat(numWord, single[int(part[0])])
        numWord = concat(numWord, 'Hundred')
    #if numWord == '':
    #    numWord += ' '
    numWord = concat(numWord, constructTwo(part[1:]))
    numWord = concat(numWord, groups[i])
    return numWord
    
def ans(N):
    if N == '0':
        return 'Zero'
    if N == '1000000000000':
        return 'One Trillion'
    l = len(N)
    N = '0'*(12-l)+N
    numWord = ''
    for i in range(4):
        numWord = concat(numWord, constructThree(N[3*i:3*i+3],i))
    numWord = trimleft(numWord)
    numWord = trimright(numWord)
    return numWord

def main():
    T = int(input().strip())
    for _ in range(T):
        N = input().strip()
        print(ans(N))

def main2():
    M = 10202 # 1012
    cases = range(M-1,M+2)
    for case in cases:
        word = ans(str(case))
        print(word)
    print("Finished!")
        
main2()        
