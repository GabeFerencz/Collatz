#!/usr/bin/env python
#Gabe Ferencz

def build(num):
    if not isinstance(num,int):
        print('Sorry: integers only')
        return
    even = num*2
    odd = (num-1)/3.0
    print '(' + formatNum(even),
    if (num-1)%3 == 0:
        print formatNum(int(odd)),
    print '\b) -> ' + formatNum(num)
    return

def dissect(num,idx=0):
    if not isinstance(num,int):
        print('Sorry: integers only')
        return
    if num == 1:
        print formatNum(num) + ' (' + str(idx),
        if idx == 1:
            print 'step)'
        else:
            print 'steps)'
        return idx
    idx = idx + 1
    if num % 2 == 0:
        newNum = num/2
    else:
        newNum = num*3+1
    print formatNum(num)+'('+str(num)+')',
    return dissect(newNum,idx)

def changeToBase(num, base, outp = ''):
    outp = str(num%base) + outp
    if num//base == 0:
        return outp
    return changeToBase(num//base, base, outp)

def formatNum(num):
    try:
        base = baseFormat
    except(NameError):
        base = 2
    if base != 10:
        return changeToBase(num,base)
    return str(num)

if __name__ == '__main__':
    import sys
    baseFormat = 2
    
    if len(sys.argv) == 2:
        inputNum = int(sys.argv[1])
        print 'Collatz breakdown of {0} in base {1}:'.format(inputNum,baseFormat)
        build(inputNum)
        count = dissect(inputNum)
#        while (count != 0):  #infinite loop at 5
#            count = dissect(count)
    else:
        build(10)
        count = dissect(10)
        build(3)
        count = dissect(3)

# 0
# 1
# 2
# 3
# 4
# 10 (5)
# 11 (6)
# 12 (7)
# 13 (8)
# 14 (9)
# 20 (10)
