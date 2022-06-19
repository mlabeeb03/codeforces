def solve():
    n = int(input())
    a = list(map(int, input().split()))
    #n, k = map(int, input().split())
    
    s = 0
    ind = 0
    while(ind < n):
        mx = mn = 0
        while ind < n and a[ind] > 0:
            mx = max(mx, a[ind])
            ind += 1
        while ind < n and a[ind] < 0:
            if mn == 0:
                mn = a[ind]
            else:
                mn = max(mn, a[ind])
            ind += 1
        s += mx
        s += mn
    print(s)
    

for _ in range(int(input())):
    solve()

    