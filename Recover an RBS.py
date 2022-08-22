import math

def isRbs(a):
    ob = cb = 0
    for i in a:
        if i == '(':
            ob += 1
        else:
            cb += 1
        if cb > ob:
            return False
    return True

def solve():
    a = list(map(str, input()))
    n = len(a)
    ob = n // 2
    cb = n // 2
    for i in range(len(a)):
        if a[i] == '(':
            ob -= 1
        elif a[i] == ')':
            cb -= 1
    indo = None
    i = 0
    while ob > 0:
        if a[i] == '?':
            a[i] = '('
            ob -= 1
            indo = i
        i += 1
    indc = math.inf
    i = 0
    while cb > 0:
        if a[i] == '?':
            a[i] = ')'
            cb -= 1
            indc = min(indc, i)
        i += 1
    if indo is None or indc is math.inf:
        print('YES')
        return
    a[indo] = ')'
    a[indc] = '('
    #print(*a)
    if isRbs(a):
        print('NO')
    else:
        print('YES')
 
for _ in range(int(input())):
    solve()



