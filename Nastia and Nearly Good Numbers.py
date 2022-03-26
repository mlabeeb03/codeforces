# -*- coding: utf-8 -*-

def solve(a, b):
    if b == 1:
        print('NO')
    else:
        print('YES')
        print(a, a*b, a*(b+1))

tcs = int(input())
for i in range(tcs):
    a, b = list(map(int, input().split()))
    solve(a, b)
    

    