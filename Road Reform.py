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
    n, m, k = inli()
    edges = [inli() for i in range(m)]
    # print(edges, end="\n\n")
    high = []
    low = []
    equal = []
    for i in range(m):
        edges[i] += [abs(edges[i][-1] - k)]
        if edges[i][2] > k:
            high.append(edges[i])
        elif edges[i][2] < k:
            low.append(edges[i])
        else:
            equal.append(edges[i])
    high.sort(key=lambda x: x[3])
    low.sort(key=lambda x: x[3])

    def find_ans(edge_list):
        parent = [i for i in range(n + 1)]
        size = [1] * (n + 1)

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

        small = big = None
        for u, v, s, d in edge_list:
            if find(u) == find(v):
                continue
            union(u, v)
            if s <= k:
                if small is None:
                    small = d
                else:
                    small = min(small, d)
            else:
                if big is None:
                    big = d
                else:
                    big += d
        # print(edge_list, small, big)
        if big is None:
            return small
        else:
            return big

    ans = None
    if len(equal) > 0:
        ans = find_ans(equal + low + high)
    elif len(low) == 0:
        ans = find_ans(high)
    elif len(high) == 0:
        ans = find_ans(low)
    else:
        ans = min(find_ans(low + high), find_ans([high[0]] + low + high[1:]))
    print(ans)


for x in range(ini()):
    solve()
