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

from collections import Counter, defaultdict, deque
from itertools import accumulate
import heapq as hq

# _____________________________________________________________

inf = float("inf")
mod = 1000000007

# _____________________________________________________________


def solve():
    n = ini()
    edges = [inli() for i in range(n - 1)]

    parent = [i for i in range(n + 1)]
    size = [1] * (n + 1)
    islands = [n + 1]

    def find(x):
        if parent[x] == x:
            return x
        parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        a, b = find(x), find(y)
        if a != b:
            if size[a] < size[b]:
                a, b = b, a
            parent[b] = a
            size[a] += b
            islands[0] -= 1

    extra = []
    for x, y in edges:
        if find(x) == find(y):
            extra.append([x, y])
        else:
            union(x, y)

    fin = set()
    for i in range(1, n + 1):
        fin.add(find(i))
    fin = list(fin)

    print(islands[0] - 2)

    for i, j in extra:
        print(i, j, fin[-1], fin[-2])
        fin.pop()


for x in range(1):
    solve()
