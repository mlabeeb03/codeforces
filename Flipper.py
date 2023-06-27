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


def bigger(ans, tmp):
    for i in range(len(ans)):
        if tmp[i] < ans[i]:
            return False
        elif tmp[i] > ans[i]:
            return True
        else:
            continue


def solve():
    n = ini()
    a = inli()
    if n == 1:
        print(*a)
        return
    ans1 = [0] * n
    ans2 = [0] * n
    mx1 = a.index(sorted(a)[-1])
    mx2 = a.index(sorted(a)[-2])
    for i in range(n):
        for j in range(i + 1, n + 1):
            if j == mx1 or j == mx1 + 1:
                tmp = a[i:j]
                for k in range(len(tmp) // 2):
                    tmp[k], tmp[len(tmp) - k - 1] = tmp[len(tmp) - k - 1], tmp[k]
                tmp = a[j:] + tmp + a[:i]
                if bigger(ans1, tmp):
                    ans1 = tmp

            if j == mx2 or j == mx2 + 1:
                tmp = a[i:j]
                for k in range(len(tmp) // 2):
                    tmp[k], tmp[len(tmp) - k - 1] = tmp[len(tmp) - k - 1], tmp[k]
                tmp = a[j:] + tmp + a[:i]
                if bigger(ans2, tmp):
                    ans2 = tmp
    if bigger(ans2, ans1):
        print(*ans1)
    else:
        print(*ans2)


for x in range(int(input())):
    solve()

# 5 4 1 3 2
# 9 4 1 6 7 2 8 5 3
# 3 2 1 4
# 1 2
# 6 5 3 2 4 1
# 7 6 4 5 3 2 1
# 9 3 8 4 7 1 10 2 5 6
# 3 4 2 1
# 1
