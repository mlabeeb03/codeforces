import math
def solve():
    n, k = map(int, input().split())
    p = 1
    ans = 0
    mod = 1000000007
    
    for i in range(32):
        if k & (1 << i):
            ans = (ans + p) % mod 
        p *= n
        p %= mod
    print(ans)

for _ in range(int(input())):
    solve()

    