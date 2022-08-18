import sys
input = sys.stdin.readline
import math
def solve():
    n = int(input())
    ans = 0
    l = 1
    for x in range(2, 100):
        ans += x * (n // l - n // math.lcm(l, x))
        l = math.lcm(l, x)
    print(ans % (10 ** 9 + 7))

for _ in range(int(input())):
    solve()

    