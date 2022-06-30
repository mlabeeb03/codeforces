def solve():
    n, k = map(int, input().split())
    #a = list(map(int, input().split()))
    
    ans = n
    j = 1
    while(j * j <= n):
        if n % j == 0:
            if j <= k:
                ans = min(ans, n // j)
            if n // j <= k:
                ans = min(ans, j)
        j += 1
    print(ans)
 
for _ in range(int(input())):
    solve()