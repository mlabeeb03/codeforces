def solve():
    n = int(input())
    s = list(map(int, input().split()))
    f = list(map(int, input().split()))
    
    res = [0 for i in range(n)]
    res [0] = f[0] - s[0]
    
    for i in range(1, n):
        if s[i] >= f[i - 1]:
            res[i] = f[i] - s[i]
        else:
            res[i] = f[i] - f[i - 1]
    print(*res)

for _ in range(int(input())):
    solve()

    