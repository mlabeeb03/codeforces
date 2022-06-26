def solve():
    #n = int(input())
    n, m = map(int, input().split())
    #a = list(map(int, input().split()))
    
    ans = 0  
    for i in range(19):
        ans = max(ans, arr[m][i] - arr[n - 1][i])
    print((m - n + 1) - ans)

N = 200001
arr = [[0 for _ in range(19)] for _ in range(N)]
for i in range(1, N):
    n = 0
    x = i
    while x > 0:
        arr[i][n] = x % 2 + arr[i - 1][n]
        x //= 2
        n += 1
        
for __ in range(int(input())):
    solve()

   