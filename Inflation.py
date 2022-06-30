import math
def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    asum = a[0]
    
    for i in range(1, n):
        ans = max(ans, (100 * a[i] - k * asum + k - 1) / k);
        asum += a[i]
    
    print(int(ans))
 
for _ in range(int(input())):
    solve()