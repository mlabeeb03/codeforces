import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")

def solve():
    n = int(input())  
    a = list(map(int, input().split()))
    x = sum(a)
    if x % 2 == 1:
        print(0)
    else:
        x //= 2
        dp = [[0 for _ in range(x + 1)] for _ in range(n)]
        dp[0][0], dp[0][a[0]] = 1, 1
        for i in range(1, n):
            for j in range(x):
                if dp[i - 1][j] == 1:
                    dp[i][j] = 1
                    if j + a[i] <= x:
                        dp[i][j + a[i]] = 1
        r = 0
        for i in range(n):
            if dp[i][x] == 1:
                r = 1
        
        if r == 0:
            print(0)
        else:
            print(1)
            while True:
                for i in range(n):
                    if a[i] % 2 == 1:
                        print(i + 1)
                        return
                for i in range(n):
                    a[i] //= 2

for _ in range(1):
    solve()

    
    

    