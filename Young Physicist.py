# -*- coding: utf-8 -*-

n = int(input())
f = [[None for i in range(3)] for i in range(n)]
for i in range(n):
    f[i] = list(map(int, input().split()))
res = [0] * 3
for i in range(n):
    res[0] += f[i][0]
    res[1] += f[i][1]
    res[2] += f[i][2]
if res[0] == res[1] == res[2] == 0:
    print('YES')
else:
    print('NO')