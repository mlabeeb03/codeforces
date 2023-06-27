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


def make_set(n, parent, size):
    for v in range(n + 1):
        parent[v] = v
        size[v] = 1


def find_set(v, parent, size):
    if v == parent[v]:
        return v
    parent[v] = find_set(parent[v], parent, size)
    return parent[v]


def union_sets(a, b, parent, size):
    a = find_set(a, parent, size)
    b = find_set(b, parent, size)
    if a != b:
        if size[a] < size[b]:
            a, b = b, a
        parent[b] = a
        size[a] += size[b]


def solve():
    n = ini()
    a = inli()
    parent, size, done = [None] * (n + 1), [None] * (n + 1), [False] * (n + 1)
    make_set(n, parent, size)

    for i in range(n):
        x, y = find_set(i + 1, parent, size), find_set(a[i], parent, size)
        if x == y and size[x] > 2 and a[a[i] - 1] != i + 1:
            done[x] = True
        else:
            union_sets(i + 1, a[i], parent, size)
        # print(i)
        # print(parent)
        # print(size)
        # print(done)
        # print()

    for i in range(n):
        x = find_set(i + 1, parent, size)

    c = list(set(parent).difference([0]))
    # print()
    # print(c)
    # print(done)
    mx = len(c)

    mn = 0
    fac = 0

    for i in c:
        if done[i] is True:
            mn += 1
        else:
            fac |= 1

    print(mn + fac, mx)


for x in range(int(input())):
    solve()

# 1 3
# 2 2
# 1 3
# 1 1
# 1 2
# 1 1
# 1 1
# 2 2
# 1 2
# 1 1
