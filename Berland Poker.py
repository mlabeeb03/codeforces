import math
for i in range(int(input())):
    n, m, k = map(int, input().split())
    if m == 0:
        print(0)
    else:
        mc = int(n/k)
        if mc >= m:
            print(m)
        else:
            print(mc - math.ceil((m-mc)/(k-1)))
    