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

from collections import Counter

# _____________________________________________________________

inf = float("inf")
mod = 1000000007

# _____________________________________________________________


def solve():
    n, m = inli()
    a = inli()
    a.sort()
    dic = Counter(a)
    a = list(set(a))
    a.sort()
    n = len(a)

    if n < m:
        print(0)
        return

    curr = 1
    for i in range(m):
        curr *= dic[a[i]]

    ans = 0
    for i in range(n - m + 1):
        if a[i + m - 1] - a[i] < m:
            ans += curr
            ans %= mod
        if i + m < n:
            curr *= dic[a[i + m]]
            curr //= dic[a[i]]
    print(ans)


for x in range(int(input())):
    solve()
