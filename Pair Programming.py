def solve():
    try:
        k, n, m = map(int, input().split())
    except:
        k, n, m = map(int, input().split())
    mon = list(map(int, input().split()))
    pol = list(map(int, input().split()))
    arr = [] * (n+m)     
    i = j = 0
    while(i<n or j<m):
        run = 0
        while(i<n and mon[i] <= k):
            if mon[i] == 0:
                k += 1
            arr.append(mon[i])
            i += 1
            run = 1
        while(j<m and pol[j] <= k):
            if pol[j] == 0:
                k += 1
            arr.append(pol[j])
            j += 1
            run = 1
        if run == 0:
            print(-1)
            return
    print(*arr)

for _ in range(int(input())):
    solve()
            
        
 