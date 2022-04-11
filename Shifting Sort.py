for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans = []
    tms = 0
    for i in range(n):
        x = a.index(min(a))
        if x == 0:
            a = a[1:]
        else:
            a = a[:x] + a[x+1:]
            tms += 1
            ans.append([i+1, i+x+1, x])
    print(tms)
    for row in ans:
        print(*row)



