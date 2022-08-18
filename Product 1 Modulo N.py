#import sys
#input = sys.stdin.readline
import math

def solve():
    n = int(input())
    #n, k = map(int, input().split())
    #a = list(map(int, input().split()))

    ans = []
    p = 1
    c = 0
    for i in range(1, n):
        if math.gcd(n, i) == 1:
            ans.append(i)
            p = (p * i) % n
            c += 1
    
    if p != 1:
        ans.remove(p)
        c -= 1
    print(c)
    print(*ans)
    
for _ in range(1):
    solve()

    