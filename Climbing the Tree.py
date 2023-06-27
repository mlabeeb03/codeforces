import sys
from math import inf
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

def do(h, a, b):
    l, r = 1, h
    ans = h
    while l <= r:
        m = (l + r) // 2
        top = a * m - (b * (m - 1))
        if top >= h:
            ans = m
            r = m - 1
        else:
            l = m + 1
    return ans

def solve():
    q = ini()
    height = [0, inf]
    ans = []
    for i in range(q):
        arr = inli()
        if arr[0] == 1:
            a, b, n = arr[1:]
            top = a * n - (b * (n - 1))
            bot = top - (a - b - 1)
            if n == 1:
                top = a
                bot = 1
            if top < height[0] or bot > height[1]:
                ans.append(0)
            else:
                height[0] = max(height[0], bot)
                height[1] = min(height[1], top)
                ans.append(1)
        else:
            a, b = arr[1:]
            x = do(height[0], a, b)
            y = do(height[1], a, b)
            if x == y:
                ans.append(x)
            else:
                ans.append(-1)
    print(*ans)

for _ in range(int(input())):
    solve()
