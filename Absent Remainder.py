# -*- coding: utf-8 -*-

tcs = int(input())
for i in range(tcs):
    n = int(input())
    nums = list(map(int, input().split()))
    m = min(nums)
    nums.remove(m)
    for j in range(int(n/2)):
        print(nums[j], m)
    