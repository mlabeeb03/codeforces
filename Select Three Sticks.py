import sys
input = lambda: sys.stdin.readline().rstrip("\r\t")
import math

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = math.inf
    
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                ans = min(ans, (a[k] - a[j]) + (a[j] - a[i]))
    print(ans)
       
for _ in range(int(input())):
    solve()
    
    

    