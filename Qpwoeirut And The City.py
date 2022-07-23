import math
def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    if n % 2 == 1:
        ans = 0
        for i in range(1, n - 1, 2):
            ans += max(max(a[i - 1], a[i + 1]) - a[i] + 1, 0)
        print(ans)
    else:
        ans = math.inf
        s1 = [None] * n
        s2 = [None] * n
        s1[1] = max(max(a[0], a[2]) - a[1] + 1, 0)
        for i in range(3, n - 1, 2):
            s1[i] = s1[i - 2] + max(max(a[i - 1], a[i + 1]) - a[i] + 1, 0)
        s2[-2] = max(max(a[-1], a[-3]) - a[-2] + 1, 0)
        for i in range(n - 4, 1, -2):
            s2[i] = s2[i + 2] + max(max(a[i - 1], a[i + 1]) - a[i] + 1, 0)
            
        for i in range(n - 2, 3, -2):
            ans = min(ans, s2[i] + s1[i - 3])
        ans = min(ans, s1[-3], s2[2])  
        print(ans)
         

for _ in range(int(input())):
    solve()