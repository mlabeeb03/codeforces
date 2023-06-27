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


def calc(fin):
    if fin <= 2:
        return fin
    else:
        return 1 + calc(fin - (fin + 1) // 2)


def do(a, x):
    fin = 0
    curr = 0
    for i in a:
        if i == x:
            curr = 0
        else:
            curr += 1
        fin = max(fin, curr)
    return calc(fin)


def solve():
    a = ins()
    ans = inf
    for i in range(96, 96 + 27):
        ans = min(ans, do(a, chr(i)))
    print(ans)


for _ in range(int(input())):
    solve()

# c o d e f o r c e s
