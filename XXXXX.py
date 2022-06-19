def solve():
    #n = int(input())
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    #a = list(map(str, input()))
    
    if sum(a) % x != 0:
        print(n)
        return
    
    flag = 0
    for i in a:
        if i % x != 0:
            flag = 1
    if flag == 0:
        print(-1)
        return
    
    l = 0
    for i in range(n):
        if a[i] % x != 0:
            l = n - (i + 1)  
            break
    m = 0
    for i in range(n - 1, -1, -1):
        if a[i] % x != 0:
            m = n - (n - i)
            break
    print(max(l, m))
    
for _ in range(int(input())):
    solve()

    