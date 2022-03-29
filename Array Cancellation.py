# -*- coding: utf-8 -*-

for i in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    s = 0
    c = 0
    for j in range(len(nums)):
        s = s + nums[j]
        if s < 0:
            c += abs(s)
            s = 0
    print(c)                         
            