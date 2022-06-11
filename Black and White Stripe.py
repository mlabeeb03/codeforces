def solve():
    #n = int(input())
    n, k = map(int, input().split())
    #s = list(map(int, input().split()))
    a = list(map(str, input()))
    
    if n == k:
        print(a.count('W'))
        return

    minn = a[0:k].count('W')
    #print(minn)
    gmin = minn
    for i in range(n - k):
        if a[i] == 'W' and a[i + k] == 'B':
            minn -= 1
            if minn < gmin:
                gmin = minn
        elif a[i] == 'B' and a[i + k] == 'W':
            minn += 1
        else:
            minn = minn
    print(gmin)

for _ in range(int(input())):
    solve()

    