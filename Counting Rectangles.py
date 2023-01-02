import sys
input = lambda: sys.stdin.readline().rstrip("\n\r")

def solve():
    n, q = map(int, input().split())
    a = []
    b = []
    dp = [[0 for i in range(nm)] for i in range(nm)]
    for i in range(n):
        x, y = map(int, input().split())
        dp[x][y] += x * y
        a.append([x, y])
    for i in range(q):
        b.append(list(map(int, input().split())))
        
    for i in range(1, nm):
        for j in range(1, nm):
            dp[i][j] += dp[i][j - 1] + dp[i - 1][j] - dp[i - 1][j - 1]
        
    for i in b:
        big = dp[i[2] - 1][i[3] - 1]
        upper = dp[i[0]][i[3] - 1]
        left = dp[i[2] - 1][i[1]]
        add = dp[i[0]][i[1]]
        print(max(0, big - upper - left + add))


nm = 1001
for _ in range(int(input())):
    solve()

    