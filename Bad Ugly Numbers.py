# -*- coding: utf-8 -*-

tcs = int(input())
for i in range(tcs):
    n = int(input())
    if n == 1:
        print(-1)
    else:
        print('2' + '3'*(n-2) + '3')


    