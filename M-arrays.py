def solve():
    #n = int(input())
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    #a = list(map(int, input()))
    
    ans = 0
    mods = [i % m for i in a]
    d = {}
    for i in mods:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    if 0 in d:
        ans += 1
        del d[0]
    if m % 2 == 0:
        if m // 2 in d:
            ans += 1
            del d[m // 2]
    for i in d.keys():
        if d[i] == 0:
            continue
        j = m - i
        if j not in d:
            ans += d[i]
            continue
        ans += max(abs(d[i] - d[j]), 1)
        d[i] = d[j] = 0
    
    print(ans)
      
for __ in range(int(input())):
    solve()

   