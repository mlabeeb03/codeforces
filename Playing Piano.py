import sys
input = lambda: sys.stdin.readline().rstrip("\r\t")

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    dp = [[6 for i in range(n)] for i in range(5)]
    for i in range(5):
        dp[i][0] = i
    move = [None] * (n - 1)
    for i in range(n - 1):
        if a[i + 1] > a[i]:
            move[i] = 1
        elif a[i + 1] < a[i]:
            move[i] = -1
        else:
            move[i] = 0
        
    for i in range(n - 1):
        for j in range(5):
            if dp[j][i] != 6:
                if move[i] == 1:
                    for k in range(j + 1, 5):
                        dp[k][i + 1] = j
                elif move[i] == -1:
                    for k in range(j - 1, -1, -1):
                        dp[k][i + 1] = j
                else:
                    for k in range(j + 1, 5):
                        dp[k][i + 1] = j
                    for k in range(j - 1, -1, -1):
                        dp[k][i + 1] = j
    
    do = -1
    for i in range(5):
        if dp[i][n - 1] < 6:
            do = i
            break
    if do == -1:
        print(-1)
        return
    
    ans = []
    for i in range(n - 1, -1, -1):
        ans.append(do + 1)
        do = dp[do][i]
        
    print(*reversed(ans))
        
for _ in range(1):
    solve()
    
    

    