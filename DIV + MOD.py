# -*- coding: utf-8 -*-

itr = int(input())
op = [0]*itr
for i in range(itr):
    l, r, a = input().split()
    l = int(l)
    r = int(r)
    a = int(a)
    if int(l/a) == int(r/a):
        op[i] = int(r/a)+r%a
    else:
        op[i] = max(int(r/a)+r%a, int(r/a-1)+a-1)
print(*op, sep='\n')


    