import sys
input = sys.stdin.readline
import math

def solve():
    n = int(input())
    l = cforl = cforr = cfors = math.inf
    r = 0
    longest = [math.inf, 0]
    arr = []
    for i in range(n):
        a, b, c = map(int, input().split())

        if a == longest[0] and b == longest[1]:
            cfors = min(cfors, c)
        elif a <= longest[0] and b >= longest[1]:
            longest[0], longest[1] = a, b
            cfors = c

        if a < l:
            l = a
            cforl = c
        if a == l:
            if c < cforl:
                cforl = c

        if b > r:
            r = b
            cforr = c
        if b == r:
            if c < cforr:
                cforr = c

        if longest[0] == l and longest[1] == r:
            print(min(cforl + cforr, cfors))
        else:
            print(cforl + cforr)
            
for _ in range(int(input())):
    solve()

    