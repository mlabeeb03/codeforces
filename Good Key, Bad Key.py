import sys
input = lambda: sys.stdin.readline().rstrip("\n\r")
from itertools import accumulate

def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    arr = list(accumulate(a))
    ans = arr[-1] - (k * n)
    #print(arr)
    #print(ans)
    for i in range(n):
        sm = None
        if i == 0:
            sm = 0
        else:
            sm = arr[i - 1] - (k * i)
        ind = 2
        for j in range(i, min(i + 50, n)):
            sm += a[j] // ind
            #print(j, a[j], ind, a[j] // ind)
            ind *= 2
        ans = max(ans, sm)
        
    
    print(ans)

for _ in range(int(input())):
    solve()
    