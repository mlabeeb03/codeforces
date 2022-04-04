for i in range(int(input())):
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    dic = {}
    for i in range(n):
        dic[i] = nums[i]
    dic = {k: v for k, v in sorted(dic.items(), key = lambda item: item[1])}
    x = list(dic.keys())
    s = 1
    for j in range(n-1):
        if x[j+1] == x[j] + 1:
            continue
        s += 1
    print('YES' if s <= k else 'No')
 