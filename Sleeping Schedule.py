import sys
input = lambda: sys.stdin.readline().rstrip("\n\r")

def solve():
    n, h, l, r = map(int, input().split())
    a = list(map(int, input().split()))
    
    dp = [[-1 for i in range(h)] for i in range(n)]
    dp[0][a[0]] = 0
    if a[0] >= l and a[0] <= r:
        dp[0][a[0]] = 1
    dp[0][a[0] - 1] = 0
    if a[0] - 1 >= l and a[0] - 1 <= r:
        dp[0][a[0] - 1] = 1
        
    for i in range(n - 1):
        for j in range(h):
            if dp[i][j] > -1:
                x = j + a[i + 1]
                if x >= h:
                    x = x - h
                dp[i + 1][x] = max(dp[i + 1][x], dp[i][j])
                if x >= l and x <= r:
                    dp[i + 1][x] = max(dp[i + 1][x], dp[i][j] + 1)
                    
                x = j + a[i + 1] - 1
                if x >= h:
                    x = x - h
                dp[i + 1][x] = max(dp[i + 1][x], dp[i][j])
                if x >= l and x <= r:
                    dp[i + 1][x] = max(dp[i + 1][x], dp[i][j] + 1)
    
    print(max(0, max(dp[n - 1])))

for _ in range(1):
    solve()

    