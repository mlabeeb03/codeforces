def solve():
    n, m = map(int, input().split())
    arr = []
    for i in range(n):
        arr.append(list(map(int, input())))
    ones = 4
    for i in range(n - 1):
        for j in range(m - 1):
            oc = 0
            if arr[i][j] == 1:
                oc += 1
            if arr[i][j + 1] == 1:
                oc += 1
            if arr[i + 1][j] == 1:
                oc += 1
            if arr[i + 1][j + 1] == 1:
                oc += 1
            ones = min(ones, oc)
    onecount = 0
    for i in arr:
        onecount += i.count(1)
    if ones <= 2:
        print(onecount)
    else:
        print(onecount - ones + 2)
    
for _ in range(int(input())):
    solve()
    
            