import sys
input = sys.stdin.readline

def solve():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    if n == 1:
        print(0)
        return
    i = 1
    ans = 0
    while i < n:
        mn = min(a[i], a[i - 1])
        mx = max(a[i], a[i - 1])
        while abs(mx - ((mx + mn) // 2)) <= x and abs(mn - ((mx + mn) // 2)) <= x:
            i += 1
            if i == n:
                print(ans)
                return
            mn = min(mn, a[i])
            mx = max(mx, a[i])
        ans += 1
        i += 1
    print(ans)
            
for _ in range(int(input())):
    solve()

    