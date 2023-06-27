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
    n, k = inli()
    a = inli()
    l, r, ans = 0, 10000000000, 10000000000

    # def do(a, m):
    #     curr = 0
    #     miss = 0
    #     ind = 0
    #     while ind < len(a):
    #         if a[ind] <= m:
    #             curr += 1
    #             miss += 1
    #             ind += 2
    #         else:
    #             if ind == len(a) - 1 and curr > 0:
    #                 miss += 1
    #             ind += 1
    #     return curr + miss

    def do(a, m):
        arr = [[], []]
        turn = 0
        ind = 0
        while ind < len(a):
            if turn == 0:
                if a[ind] <= m:
                    arr[turn].append(a[ind])
                    turn = 1 - turn
            elif turn == 1:
                arr[turn].append(a[ind])
                turn = 1 - turn
            ind += 1
        return len(arr[0]) + len(arr[1])

    def pos(m):
        if do(a, m) >= k:
            return True
        elif 1 + do(a[1:], m) >= k:
            return True
        else:
            return False

    while l <= r:
        m = (l + r) // 2
        if pos(m):
            ans = m
            r = m - 1
        else:
            l = m + 1
    print(ans)


for _ in range(1):
    solve()
