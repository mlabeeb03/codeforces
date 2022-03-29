# -*- coding: utf-8 -*-

tcs = int(input())
for i in range(tcs):
    x, y = map(int, input().split())
    a, b = map(int, input().split())
    if x < y:
        x, y = y, x
    if(b >= a * 2):
        print(a * (x + y))
    else:
        print(y * b + (x - y) * a)
    