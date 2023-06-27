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

from collections import Counter, defaultdict
from itertools import accumulate

# _____________________________________________________________

inf = float("inf")
mod = 1000000007

# _____________________________________________________________


def solve():
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    dic = defaultdict(int)
    for i in a:
        x = [i for i in dic.keys()]
        y = [i for i in dic.values()]
        # for j in range(len(x)):
        #     dic[i & x[j]] += y[j]
        #     dic[i & x[j]] %= mod
        for l, m in zip(x, y):
            dic[i & l] += m
            dic[i & l] %= mod
        dic[i] += 1
        dic[i] %= mod
        # print(dic)
    ans = 0
    for i in dic:
        if onbits[i] == k:
            ans += dic[i]
            ans %= mod
    print(ans % mod)


onbits = [(bin(i).replace("0b", "")).count("1") for i in range(64)]
for x in range(int(input())):
    solve()

# 5 0 3 1 7 3 2
