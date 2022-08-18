def solve():
    n = int(input())
    a = list(map(int, input().split()))
    ans = n - 1
    for i in range(n - 1):
        for j in range(i + 1, n):
            x = 0
            for k in range(j):
                if a[j] - a[k] != (j - k) * (a[j] - a[i]) / (j - i):
                    x += 1
            for k in range(j + 1, n):
                if a[k] - a[j] != (k - j) * (a[j] - a[i]) / (j - i):
                    x += 1
            ans = min(ans, x)
    print(ans)
 
for _ in range(int(input())):
    solve()