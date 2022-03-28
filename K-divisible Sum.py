# -*- coding: utf-8 -*-

tcs = int(input())
for i in range(tcs):
    n, k = list(map(int, input().split()))
    cf = int((n+k-1)/k)
    k *= cf
    print(int((k+n-1)/n))

    