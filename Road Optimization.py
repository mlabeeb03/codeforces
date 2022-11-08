import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")
import math

n, l, k = map(int, input().split())
d = list(map(int, input().split())) + [l]
a = list(map(int, input().split())) + [0]
dp = [[0] * (k + 1) for i in range(n + 1)]   
  
for i in range(n - 1, -1, -1):
    for kk in range(k + 1):
        dp[i][kk] = math.inf
        for j in range(i + 1, n + 1):
            if j - i - 1 > kk:
                break
            dp[i][kk] = min(dp[i][kk], a[i] * (d[j] - d[i]) + dp[j][kk - (j - i - 1)])
print(dp[0][k])
        





