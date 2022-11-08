import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")
from math import isqrt

def find(r):
    x = isqrt(r)
    ans = x * 3
    a = x * x + x
    b = x * x + (2 * x)
    if r >= b:
        ans -= 0
    elif r >= a:
        ans -= 1
    else:
        ans -= 2
    return ans

def solve():
    l, r = map(int, input().split())
    print(find(r) - find(l - 1))
      
for _ in range(int(input())):
    solve()