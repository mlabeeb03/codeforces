import bisect 
for _ in range(int(input())):
    n, l, r = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
 
    ans1 = ans2 = 0    
    for i in range(n):
        x = r - a[i]
        y = (l - a[i]) - 1
        ans1 += n - bisect.bisect_right(a, x, lo=i+1, hi=n)
        ans2 += n - bisect.bisect_right(a, y, lo=i+1, hi=n)
    print(ans2 - ans1)