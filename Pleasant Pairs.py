import collections
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    #a = list(map(int, input()))
    d = {}
    for i in range(n):
        d[a[i]] = i+1
    od = collections.OrderedDict(sorted(d.items()))
    nums = list(od.keys())
    inds = list(od.values())
    ans = 0
    for i in range(n-1):
        for j in range(i+1,n):
            if nums[i]*nums[j] == inds[i]+inds[j]:
                ans += 1
            if nums[i]*nums[j]>2*n:
                break;
    print(ans)


