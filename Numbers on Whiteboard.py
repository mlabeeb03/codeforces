# -*- coding: utf-8 -*-
import math
tcs = int(input())
for i in range(tcs):
    n = int(input())
    print(2)
    if n == 2:
        print(1, 2)
    else:
        m = n
        arr = [None]*n
        for i in range(n):
            arr[i] = m
            m -= 1
        for i in range(n-1):
            print(arr[i], arr[i+1])
            arr[i+1] = math.ceil((arr[i] + arr[i+1]) / 2)

    