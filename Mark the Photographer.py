def solve():
    n, x = map(int, input().split())    
    a = list(map(int, input().split()))
    
    a.sort()
    for i in range(n):
        if a[n+i] - a[i] < x:
            print('NO')
            return
    print('YES')

for _ in range(int(input())):
    solve()

    