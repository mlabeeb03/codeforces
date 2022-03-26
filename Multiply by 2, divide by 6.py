# -*- coding: utf-8 -*-

n = int(input())
for i in range(n):
    x = int(input())
    n2f = n3f = 0
    while x % 2 == 0:
        x /= 2
        n2f += 1
    while x % 3 == 0:
        x /= 3
        n3f += 1
    if x == 1 and n2f <= n3f:
        print(2 * n3f - n2f)
    else:
        print(-1)

