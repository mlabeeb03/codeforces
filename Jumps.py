def solve():
    n = int(input())
    #n, m = map(int, input().split())
    #a = list(map(int, input().split()))
    #a = list(map(int, input()))
    
    ans = 0
    while(ans * (ans + 1) < 2 * n):
        ans += 1
    if (ans * (ans + 1)) // 2 == n + 1:
        ans += 1
    print(ans)
      
for __ in range(int(input())):
    solve()

   