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

from math import inf
from collections import deque, Counter
import heapq as hq

# _____________________________________________________________


def solve():
    n = ini()
    a = ins()
    if n % 2 == 1:
        print(-1)
    else:
        c = Counter(a)
        if max(c.values()) > n // 2:
            print(-1)
        else:
            dic = {}
            pairs = []
            for i in range(n // 2):
                if a[i] == a[n - i - 1]:
                    pairs.append(a[i])
                    if a[i] in dic:
                        dic[a[i]] += 1
                    else:
                        dic[a[i]] = 1
            queue = []
            for i in dic.values():
                hq.heappush(queue, -i)
            ans = 0
            while queue:
                x = y = 0
                x = -hq.heappop(queue)
                if queue:
                    y = -hq.heappop(queue)
                if y == 0:
                    ans += x
                else:
                    ans += 1
                    x -= 1
                    y -= 1
                    if x > 0:
                        hq.heappush(queue, -x)
                    if y > 0:
                        hq.heappush(queue, -y)
            print(ans)


for _ in range(int(input())):
    solve()
