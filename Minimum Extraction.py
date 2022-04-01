# -*- coding: utf-8 -*- 
    
tcs = int(input())
for i in range(tcs):
    n = int(input())
    nums = sorted(list(map(int, input().split())))
    ans = nums[0]
    for i in range(n-1):
        ans = max(ans, nums[i+1] - nums[i])
    print(ans)
    