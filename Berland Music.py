
for i in range(int(input())):
    n = int(input())
    p = list(map(int, input().split()))
    s = list(map(int, input()))

    l = sorted([[s[i], p[i], i] for i in range(n)])
    q = [-1] * n
    for i in range(n):
        q[l[i][2]] = i + 1
    print(*q)
        
    