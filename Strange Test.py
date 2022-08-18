import sys
input = sys.stdin.readline

def solve():
    a, b = map(int, input().split())
    #a = list(map(int, input().split()))
    
    ans = b - a
    x = list(map(int, format(a, '020b')))
    y = list(map(int, format(b, '020b')))

    xind = -1
    zind = 20
    for i in range(19, -1, -1):
        if x[i] == 1 and y[i] == 0:
            x[i] = 0
            xind = i
    for i in range(xind - 1, -1, -1):
        if x[i] == 0 and y[i] == 1:
            x[i] = 1
            zind = i
            break
    for i in range(zind + 1, 20):
        x[i] = 0
    p = int(''.join(str(i) for i in x), 2)
    if p >= a:
        ans = min(ans, (p - a) + 1)
        
    x = list(map(int, format(a, '020b')))
    y = list(map(int, format(b, '020b')))
    
    yind = 20
    for i in range(19, -1, -1):
        if x[i] == 1 and y[i] == 0:
            y[i] = 1
            yind = i
    for i in range(yind + 1, 20):
        if x[i] == 0 and y[i] == 1:
            y[i] = 0
    q = int(''.join(str(i) for i in y), 2)
    if q >= b:
        ans = min(ans, (q - b) + 1)
        
    print(ans)
            
for _ in range(int(input())):
    solve()

    