import sys
try:
    file = open('inp.txt', 'r')
    input = lambda: file.readline().rstrip("\n\r")
except:
    input = lambda: sys.stdin.readline().rstrip("\n\r")

# _____________________________________________________________

def ini():
    return(int(input()))
def inl():
    return([i for i in input().split()])
def inli():
    return([int(i) for i in input().split()])
def ins():
    return([i for i in input()])
def insi():
    return([int(i) for i in input()])

# _____________________________________________________________

from math import inf
from collections import deque

# _____________________________________________________________

def solve():
    a, b = inli()
    ans = a + b + 10
    for i in range(1, 100001):
        cost = i - 1
        cost += (a + i - 1) // i
        cost += (b + i - 1) // i
        ans = min(ans, cost)
    print(ans)

for _ in range(int(input())):
    solve()
