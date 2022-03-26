# -*- coding: utf-8 -*-

tcs = int(input())
for i in range(tcs):
    n = int(input())
    nums = list(map(int, input().split()))
    nums.reverse()
    count = 0
    big = max(nums)
    thr = nums[0]
    for j in range(len(nums)-1):
        if nums[j] == big:
            break
        if nums[j] <= thr and nums[j+1] > thr:
            thr = nums[j+1]
            count += 1
    print(count)

    