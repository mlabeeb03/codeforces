def solve():
    n = int(input())
    #n, x = map(int, input().split())
    a = list(map(int, input().split()))
    #a = list(map(str, input()))
    
    a.reverse()
    l = 1
    for i in range(n-1):
        if a[i] >= a[i+1]:
            l += 1
            continue
        break
    l = n - l
    
    ind = 0
    m = 1
    while(ind < n-1 and a[ind] <= a[ind+1]):
        m += 1
        ind += 1
    while(ind < n-1 and a[ind] >= a[ind+1]):
        m += 1
        ind += 1
    m = n - m
    print(min(l, m))           
    
for _ in range(int(input())):
    solve()

    