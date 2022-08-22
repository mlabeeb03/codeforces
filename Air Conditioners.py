import math
for _ in range(int(input())):
    input()
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    t = list(map(int, input().split()))
    c = [math.inf] * n
    for i, j in zip(p, t):
        c[i - 1] = j  
    l = [None] * n
    r = [None] * n    
    x = math.inf
    for i in range(n):
        x = min(x + 1, c[i])
        l[i] = x
    x = math.inf
    for i in range(n - 1, -1, -1):
        x = min(x + 1, c[i])
        r[i] = x
    for i in range(n):
        print(min(l[i], r[i]), end = ' ')
    print()
            