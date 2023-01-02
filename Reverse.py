import sys
input = lambda: sys.stdin.readline().rstrip("\n\r")

def DecimalToBinary(num, a):
    if num >= 1:
        DecimalToBinary(num // 2, a)
    a.append(num % 2)
def OnlyOnes(s):
    if s[-1] == '#':    return False
    for i in s:
        if i == '0':    return False
    return True
def check(x, y):
    if OnlyOnes(y.replace(x, '#')) == True:
        print('YES')
        return True
    return False
def NewOnlyOnes(s):
    for i in s:
        if i == '0':    return False
    return True
def Newcheck(x, y):
    if NewOnlyOnes(y.replace(x, '')) == True:
        print('YES')
        return True
    return False
def solve():  
    x, y = list(map(int, input().split()))
    if x == y:
        print('YES')
        return
    a = []
    DecimalToBinary(x, a)
    x = ''.join(str(i) for i in a[1:])
    b = []
    DecimalToBinary(y, b)
    y = ''.join(str(i) for i in b[1:])
    
    if x[-1] == '0':
        x1 = x
        x2 = x + '1'
        x3 = x2[::-1]
        ind = x.rindex('1')
        x4 = x[:ind + 1]
        x5 = x4[::-1]
        lst = [x1, x2, x3, x4, x5]
        if x1 in y:
            if check(x1, y):
                return
        for i in lst[1:]:
            if i in y:
                if Newcheck(i, y):
                    return
    else:
        if Newcheck(x, y):
            return
        x1 = x[::-1]
        if Newcheck(x1, y):
            return
 
    print('NO')    

for _ in range(1):
    solve()


    