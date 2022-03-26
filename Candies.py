# -*- coding: utf-8 -*-

itr = int(input())
op = [0]*itr
for i in range(itr):
    l, r, a = input().split()
    l = int(l)
    r = int(r)
    a = int(a)
    op[i] = 0
    for j in range(l,r+1):
        temp = int(j/a) + j%a
        if temp > op[i]:
            op[i] = temp
print(*op, sep='\n')


    