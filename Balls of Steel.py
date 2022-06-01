def solve():
    n, k = map(int, input().split())
    a = [[] for _ in range(n)]
    for _ in range(n):
        a[_] = list(map(int, input().split()))
   
    for i in range(n):
        x = 0
        for j in range(n):
            if abs(a[i][0] - a[j][0]) + abs(a[i][1] - a[j][1]) > x:
                x = abs(a[i][0] - a[j][0]) + abs(a[i][1] - a[j][1])
        if x <= k:
            print(1)
            return
    print(-1)

for __ in range(int(input())):
    solve()
                
    
    