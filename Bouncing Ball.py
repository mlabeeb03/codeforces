import sys
input = lambda: sys.stdin.readline().rstrip("\n\r")
from math import inf

def solve():
    n, p, k = map(int, input().split())
    a = [2] + list(map(int, input())) + [2] * k
    x, y = map(int, input().split())
    pre = [inf] * (n + 1)
    pre[0] = 0
    for i in range(1, n - p + 1):
        pre[i] = pre[i - 1] + y
    #print(a)
    #print(pre)
    
    ans = inf
    for i in range(n + 1, n + k + 1):
        la = 0
        for j in range(i, 0, -k):
            try:
                ans = min(ans, pre[j - p] + la)
            except:
                pass
            try:
                if a[j - k] == 0:                    
                    la += x
            except:
                pass
            #print(j, a[j], la)
        #print()
    print(ans)

    
for _ in range(int(input())):
    solve()