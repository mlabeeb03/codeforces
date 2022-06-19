def solve():
    a = list(map(int, input()))
    n = len(a)
    
    if a.count(1) == 0 or a.count(2) == 0 or a.count(3) == 0:
        print(0)
        return
    
    ans = 200001
    x = y = 0
    while(x + 2 < n):
        while(a[x] == a[x+1]):
            x += 1
            if x == n - 1:
                print(ans)
                return
        y = x + 1
        while(a[y] == a[y+1]):
            y += 1
            if y == n - 1:
                print(ans)
                return
        if a[x] != a[y] and a[x] != a[y+1]:
            ans = min(ans, y - x + 2)
        x = y
    print(ans)

for _ in range(int(input())):
    solve()

    