import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")
from bisect import bisect_left

def solve():
    n = int(input())  
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    dmin = []
    dmax = []
    poss = [-1]

    for i in a:
        x = bisect_left(b, i)
        dmin.append(b[x] - i)
    print(*dmin)
    
    for i in range(1, n):
        if b[i - 1] - a[i] < 0:
            poss.append(i - 1)
    poss.append(n - 1)
    
    poslen = len(poss)
    p1 = 0 # poss[0]
    p2 = 0
    while p1 < poslen:
        while p2 <= poss[p1]:
            dmax.append(b[poss[p1]] - a[p2])
            p2 += 1
        p1 += 1
    print(*dmax)

for _ in range(int(input())):
    solve()

    
    

    