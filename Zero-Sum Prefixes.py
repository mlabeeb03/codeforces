import sys
input = lambda: sys.stdin.readline().rstrip("\n\r")
from collections import Counter

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    pre = [a[0]]
    for i in range(1, n):
        pre.append(pre[-1] + a[i])
            
    zind = []
    for i in range(n):
        if a[i] == 0:
            zind.append(i)
    zind.append(n)
    
    ans = pre[:zind[0]].count(0)
    for i in range(len(zind) - 1):
        x = sorted(pre[zind[i]: zind[i + 1]])
        ans += max(Counter(x).values())

    print(ans)
    
for _ in range(int(input())):
    solve()

    