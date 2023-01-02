import sys
input = lambda: sys.stdin.readline().rstrip("\n\r")
from math import gcd

def solve(): 
    n = int(input())
    a = set(list(map(int, input().split())))
    lim = max(a)
    ans = 0
    
    for i in range(lim, 0, -1):
        if i in a:
            continue
        mul = []
        for j in range(i * 2, lim + 1, i):
            if j in a:
                mul.append(j)
        
        try:
            g = mul[0]
        except:
            pass
        for x in mul[1:]:
            g = gcd(g, x)
            if g == i:
                ans += 1
                a.add(i)
                break
    print(ans)

for _ in range(1):
    solve()


    