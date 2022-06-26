def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    m = min(a)
    pos = a.index(m)
    
    print(n - 1)
    
    for i in range(n):
        if i == pos:
            continue
        ans = [pos + 1, i + 1, m, m + abs(i - pos)]
        print(*ans)
    

for _ in range(int(input())):
    solve()

    