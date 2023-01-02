import sys
input = lambda: sys.stdin.readline().rstrip("\n\r")
from math import perm, comb

def stox(x, i):
    try:
        sxavb = x - 1
        sxreq = i - 1
        return comb(sxavb, sxreq)
    except:
        return 0

def bwxy(x, y, i, j):
    try:
        xyavb = abs(x - y) - 1
        xyreq = j - i - 1
        return comb(xyavb, xyreq)
    except:
        return 0

def ytoe(x, y, i, j, n):
    try:
        yeavb = y - x - 1
        yereq = n - j - (x - i)
        return comb(yeavb, yereq)
    except:
        return 0
    
def kmore(n, i, j, x, y, k):
    sxtot = stox(x, i)
    xytot = bwxy(x, y, i, j)
    yktot = bwxy(y, n, j, k)   
    return (sxtot * xytot * yktot)

def kmid(n, i, j, x, y, k):
    sxtot = stox(x, i)
    yetot = ytoe(x, y, i, j, n)
    bw = bwxy(n, y, k, j)
    
    return (sxtot * bw * yetot)
    
def solve():  
    n, i, j, x, y = list(map(int, input().split()))
    if x > y:
        i, j, x, y = n - j + 1, n - i + 1, y, x
        
    if y == n:
        if j == n:
            print(0)
        else:
            print((comb(x - 1, i - 1) * comb(y - x - 1, j - i - 1)) % mod)
        return
    ans = 0
    for k in range(2, n):
        if k == j:
            continue
        if k < j:
            ans += kmid(n, i, j, x, y, k) % mod
        else:
            ans += kmore(n, i, j, x, y, k) % mod
    print(ans % mod)
    
mod = 1000000007
for _ in range(int(input())):
    solve()


    