def solve():
    #n = int(input())
    n, c = map(int, input().split())
    l = list(map(int, input().split()))
    a = [0] * 100
    for i in l:
        a[i - 1] += 1
    ans = 0
    #print(a)
    for i in a:
        if i == 0:
            continue
        if c <= i:
            ans += c
        else:
            ans += i
    print(ans)
      
for _ in range(int(input())):
    solve()

    