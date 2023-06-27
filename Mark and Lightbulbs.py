import sys
try:
    file = open('inp.txt', 'r')
    input = lambda: file.readline().rstrip("\n\r")
except:
    input = lambda: sys.stdin.readline().rstrip("\n\r")
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
def inv():
    return(map(int,input().split()))

from collections import deque
def solve():
    n = ini()
    s, t = insi(), insi()
    if s[0] != t[0] or s[-1] != t[-1]:
        print(-1)
    else:
        pos_s, pos_t = [], []
        for i in range(n-1):
            if s[i] != s[i+1]:
                pos_s.append(i)
            if t[i] != t[i+1]:
                pos_t.append(i)
        if len(pos_s) != len(pos_t):
            print(-1)
        else:
            print(sum(abs(x-y) for x, y in zip(pos_s, pos_t)))

for _ in range(int(input())):
    solve()
