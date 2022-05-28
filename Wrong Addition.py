def solve():
    a, s = map(int, input().split())
    ans = []
    while s:
        x = a % 10
        y = s % 10
        if x <= y:
            ans.append(y - x)
        else:
            s //= 10
            y += 10 * (s % 10)
            if x < y and y >= 10 and y <= 19:
                ans.append(y - x)
            else:
                print(-1)
                return
        a //= 10
        s //= 10
    if a:
        print(-1)
    else:
        while ans[-1] == 0:
            ans.pop()
        print(''.join(str(i) for i in reversed(ans)))
for _ in range(int(input())):
    solve()

    