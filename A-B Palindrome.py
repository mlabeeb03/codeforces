def solve():
    a, b = map(int, input().split())
    s = list(input())
    
    if a % 2 == 1 and b % 2 == 1:
        print(-1)
        return
    spl = 0
    n = len(s)
    for i in range(n // 2):
        if spl: break
        if s[i] == '?' and s[n - 1 - i] == '?': continue
        elif s[i] != '?' and s[n - 1 - i] != '?':
            if s[i] != s[n - 1 - i]: spl = 1
            if s[i] == '0': a -= 2
            else: b -= 2
        elif s[i] == '?':
            s[i] = s[n - 1 - i]
            if s[i] == '0': a -= 2
            else: b -= 2
        elif s[n - 1 - i] == '?':
            s[n - 1 - i] = s[i]
            if s[i] == '0': a -= 2
            else: b -= 2
    if spl:
        print(-1)
        return
    spl = 0
    if n % 2 == 1 and s[n // 2] == '?':
        if a % 2 == 1:
            s[n // 2] = '0'
            a -= 1
        elif b % 2 == 1:
            s[n // 2] = '1'
            b -= 1
        else:
            spl = 1
    elif n % 2 == 1:
        if s[n // 2] == '0': a -= 1
        else: b -= 1
    if spl:
        print(-1)
        return
    spl = 0
    for i in range(n // 2):
        if spl: break
        if s[i] == '?':
            if a > 1:
                s[i] = s[n - 1 - i] = '0'
                a -= 2
            elif b > 1:
                s[i] = s[n - 1 - i] = '1'
                b -= 2
            else:
                spl = 1
    if spl:
        print(-1)
        return
    if a == 0 and b == 0:
        print(''.join(s))
    else:
         print(-1)       

for _ in range(int(input())):
    solve()