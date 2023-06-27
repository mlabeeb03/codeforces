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
    n = ini()
    a = inli()
    cnt = Counter(sorted(a))
    ans = 0
    for i in cnt:
        ans += cnt[i] * (cnt[i] - 1) * (cnt[i] - 2)
        for j in range(2, 1000001):
            if i * j * j > 1000000:
                break
            ans += cnt[i] * cnt[i * j] * cnt[i * j * j]
    print(ans)


for x in range(int(input())):
    solve()
