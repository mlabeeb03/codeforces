#import sys
#input = sys.stdin.readline

def solve():
    n = int(input())
    #n, k = map(int, input().split())
    o = list(map(int, input().split()))
    #a = list(map(int, input()))
    ans = 1
    l, r = 1, mx
    while l <= r:
        a = o[:]
        m = (l + r) // 2
        succ = 1
        for i in range(n - 1, 1, -1):
            if a[i] >= m:
                avb = a[i] - m
                avb = min(avb, o[i])
                avb //= 3
                a[i] -= avb * 3
                a[i - 1] += avb
                a[i - 2] += avb * 2
            else:
                succ = 0
                break
        if succ == 1 and a[0] >= m and a[1] >= m:
            ans = max(ans, m)
            l = m + 1
        else:
            r = m - 1
    print(ans)
    
mx = int(10E9)    
for _ in range(int(input())):
    solve()

    