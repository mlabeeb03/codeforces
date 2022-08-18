import math

def getRatios(a, b):
    g = math.gcd(a, b)
    a //= g
    b //= g
    return (a, b)

def solve():
    n = int(input())
    #n, x = map(int, input().split())    
    #a = list(map(int, input().split()))
    a = list(map(str, input()))
    dc = [0] * n
    kc = [0] * n
    for i in range(n - 1):
        if a[i] == 'D':
            dc[i] += 1
            dc[i + 1] = dc[i]
            kc[i + 1] = kc[i]
        else:
            kc[i] += 1
            kc[i + 1] = kc[i]
            dc[i + 1] = dc[i]
    if a[n - 1] == 'D':
        dc[n - 1] += 1
    else:
        kc[n - 1] += 1
    ratios = {}
    for i in range(n):
        l = getRatios(dc[i], kc[i])
        if l in ratios:
            ratios[l] += 1
        else:
            ratios[l] = 1
        print(ratios[l], end = ' ')
    print()

for _ in range(int(input())):
    solve()

    