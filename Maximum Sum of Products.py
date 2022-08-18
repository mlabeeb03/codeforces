import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    #n, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    f = [None] * n
    bk = [None] * n
    f[0] = a[0] * b[0]
    bk[-1] = a[-1] * b[-1]
    for i in range(1, n):
        f[i] = f[i - 1] + a[i] * b[i]
    for i in range(n - 2, -1, -1):
        bk[i] = bk[i + 1] + a[i] * b[i]
    
    ans = bk[0]
    for i in range(n):
        cur = a[i] * b[i]
        l, r = i - 1, i + 1
        while l >= 0 and r < n:
            cur += a[l] * b[r]
            cur += b[l] * a[r]
            s = 0 if l == 0 else f[l - 1]
            t = 0 if r == n - 1 else bk[r + 1]
            ans = max(ans, cur + s + t)
            l -= 1
            r += 1
        cur = 0
        l, r = i, i + 1
        while l >= 0 and r < n:
            cur += a[l] * b[r]
            cur += b[l] * a[r]
            s = 0 if l == 0 else f[l - 1]
            t = 0 if r == n - 1 else bk[r + 1]
            ans = max(ans, cur + s + t)
            l -= 1
            r += 1
    print(ans)
    
for _ in range(1):
    solve()

    