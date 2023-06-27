import sys
try:
    file = open('inp.txt', 'r')
    input = lambda: file.readline().rstrip("\n\r")
except:
    input = lambda: sys.stdin.readline().rstrip("\n\r")   

from math import comb
def solve():
    n = int(input())
    if n == 1: print(1)
    elif n == 2: print(2)
    else:
        ans = 2
        for i in range(2, n):
            before = i - 1
            after = n - i
            total = before + after
            ans += comb(total, before)
        print(ans)


for _ in range(int(input())):
    solve()
