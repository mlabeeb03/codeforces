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
    n, m = inli()
    adj = [[] for i in range(n)]
    for i in range(m):
        x, y, z = inli()
        x, y = x - 1, y - 1
        adj[x].append([y, z])
        adj[y].append([x, z])
    start = 0
    distance = [inf] * n
    parent = [-1] * n
    distance[start] = 0
    queue = [(0, start)]
    while queue:
        dist, v = hq.heappop(queue)
        if dist > distance[v]:
            continue
        for edge in adj[v]:
            to, dist = edge
            if distance[v] + dist < distance[to]:
                distance[to] = distance[v] + dist
                parent[to] = v
                hq.heappush(queue, [distance[to], to])

    if distance[n - 1] is inf:
        print(-1)
        return
    path = deque([])
    curr = n - 1
    while curr != 0:
        path.appendleft(curr + 1)
        curr = parent[curr]
    path.appendleft(1)
    print(*path)


for x in range(1):
    solve()
