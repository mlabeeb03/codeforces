for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    s = sum(a)
    cnt = {}
    for i in a:
        cnt[i] = cnt[i] + 1 if i in cnt else 1
    if (2 * s) % n != 0:
        print(0)
        continue
    need = (2 * s) // n
    ans = 0
    for i in range(n):
        a1 = a[i]
        a2 = need - a1
        if a2 in cnt:
            ans += cnt[a2]
        if a1 == a2:
            ans -= 1
    print(ans//2)