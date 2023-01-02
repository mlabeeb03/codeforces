from math import gcd
for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    for x in range(a+1, c+1):
        y = a*b // gcd(a*b, x)
        y = y * (d//y)
        if b < y <= d:
            print(x, y)
            break
    else:
        print(-1, -1)