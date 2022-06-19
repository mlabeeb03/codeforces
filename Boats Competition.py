def solve():
    n = int(input())
    #n, l, r = map(int, input().split())
    a = list(map(int, input().split()))
    m = [0] * (n + 1)
    for i in a:
        m[i] += 1
    mx = 0
    for s in range(2, 2 * n + 1):
        cur = 0
        for i in range(1, (s + 1) // 2):
            if s - i <= n:
                cur += min(m[i], m[s-i])
        if s % 2 == 0:
            cur += m[s // 2] // 2
        mx = max(mx, cur)
    print(mx)
for __ in range(int(input())):
    solve()
    