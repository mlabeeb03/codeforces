def solve():
    #a = list(map(int,input().split()))
    a = list(map(int,input()))
    n = len(a)
    
    ones = a.count(1)
    zeros = a.count(0)
    zarr = [0] * n
    oarr = [0] * n
    
    if a[0] == 0:
        zarr[0] = 1
    else:
        oarr[0] = 1
    for i in range(1, n):
        if a[i] == 0:
            zarr[i] = zarr[i - 1] + 1
            oarr[i] = oarr[i - 1]
        else:
            zarr[i] = zarr[i - 1]
            oarr[i] = oarr[i - 1] + 1
    ans = n
    for i in range(n):
        ans = min(ans, oarr[i] + (zeros - zarr[i]))
        ans = min(ans, zarr[i] + (ones - oarr[i]))

    print(ans)
    
for __ in range(int(input())):
    solve()
     