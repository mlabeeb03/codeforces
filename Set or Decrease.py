import sys
input = sys.stdin.readline

def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()

    rsm = [None] * n
    rsm[-1] = a[-1]
    for i in range(n - 2, -1, -1):
        rsm[i] = a[i] + rsm[i + 1]
    tsm = rsm[0]
    if tsm <= k:
        print(0)
        return
    ans = tsm - k

    for i in range(1, n):
        curr = tsm - rsm[n - i] + (a[0] * i)
        times = 0
        diff = curr - k
        if diff > 0:
            times = diff // (i + 1) + ((diff % (i + 1)) != 0)
        ans = min(ans, i + times)
    print(ans)   
              
for _ in range(int(input())):
    solve()

    