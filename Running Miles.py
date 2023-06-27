import sys

try:
    file = open("inp.txt", "r")
    input = lambda: file.readline().rstrip("\n\r")
except:
    input = lambda: sys.stdin.readline().rstrip("\n\r")

# _____________________________________________________________


def ini():
    return int(input())


def inl():
    return [i for i in input().split()]


def inli():
    return [int(i) for i in input().split()]


def ins():
    return [i for i in input()]


def insi():
    return [int(i) for i in input()]


# _____________________________________________________________

from collections import Counter, defaultdict
from itertools import accumulate

# _____________________________________________________________

inf = float("inf")
mod = 1000000007

# _____________________________________________________________


def solve():
    n = ini()
    a = inli()
    pre = [a[0] + 0]
    for i in range(1, n):
        pre.append(max(pre[-1], a[i] + i))
    suf = [0] * n
    suf[-1] = a[-1] - (n - 1)
    for i in range(n - 2, -1, -1):
        suf[i] = max(suf[i + 1], a[i] - i)
    ans = 0
    for i in range(1, n - 1):
        ans = max(ans, a[i] + pre[i - 1] + suf[i + 1])
    print(ans)


for x in range(int(input())):
    solve()
