# -*- coding: utf-8 -*-

for i in range(int(input())):
    n = int(input())
    b = list(map(int, input().split()))
    if n == len(set(b)):
        print('no')
    else:
        print('yes')
    