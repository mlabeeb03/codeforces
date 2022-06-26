def solve():
    #n = int(input())
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = sum(a[:n-2*k])
    for i in range(k):
        ans += (a[i+n-2*k] // a[i+n-k])
            
    print(ans)   

for __ in range(int(input())):
    solve()

   