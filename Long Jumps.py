def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    dp = [None for _ in range(n)]    
    ans = 0
    
    for i in range(n-1, -1, -1):
        s = 0      
        j = i
        while j < n:
            if dp[j] is None:
                s = dp[j] = a[j]
            else:
                s += dp[j]
                dp[i] += dp[j]
                break
            j += a[j]
        if s > ans:
            ans = s
    print(ans)
        
    
for __ in range(int(input())):   
    solve()
                
    
    