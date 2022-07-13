def solve():
    #n, k = map(int, input().split())    
    a = list(map(str, input()))
    l = len(a)
    ans = 0
    num = 1
    if l == 1:
        print(0)
        return
    if l == 2:
        print(1 if a[0] == a[1] else 0)
        return
    for i in range(2, l):
        if a[i - 1] == a[i - 2]:
            a[i - 1] = str(num)
            num += 1
            ans += 1
        if a[i] == a[i - 2]:
            a[i] = str(num)
            num += 1
            ans += 1
    if a[-1] == a[-2]:
        ans += 1
    print(ans)            
    
for _ in range(int(input())):
    solve()

    