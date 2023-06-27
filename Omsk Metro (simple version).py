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
from collections import deque

# _____________________________________________________________


def solve():
    n = ini()
    stat = [None] * (n + 10)
    # min_suf, max_suf, min_and, max_ans
    stat[1] = [0, 1, 0, 1]
    new = 2
    for i in range(n):
        a = inl()
        if a[0] == "+":
            v, w = int(a[1]), int(a[2])
            par = stat[v]
            child = [None] * 4
            child[0] = min(0, par[0] + w)
            child[1] = max(0, par[1] + w)
            child[2] = min(child[0], par[2])
            child[3] = max(child[1], par[3])
            stat[new] = child[:]
            new += 1
        elif a[0] == "?":
            v, k = int(a[2]), int(a[3])
            if k >= stat[v][2] and k <= stat[v][3]:
                print("Yes")
            else:
                print("No")
        # print(a)
        # print(stat)
        # print()


for _ in range(int(input())):
    solve()
