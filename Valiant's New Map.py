import sys
input = lambda: sys.stdin.readline().rstrip("\n\r")

def poss(n, m, arr, val):
    brr = [[0 for i in range(m + 1)] for i in range(n + 1)]
    for i in range(n):
        for j in range(m):
            if arr[i][j] >= val:
                brr[i + 1][j + 1] = 1
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            brr[i][j] = brr[i][j] + brr[i - 1][j] + brr[i][j - 1] - brr[i - 1][j - 1]
    
    for i in range(1, n - val + 2):
        for j in range(1, m - val + 2):
            if brr[i + val - 1][j + val - 1] - (brr[i - 1][j + val - 1] + brr[i + val - 1][j - 1]) + brr[i - 1][j - 1] == val * val:
                return True
    return False

def solve(): 
    n, m = list(map(int, input().split()))
    arr = []
    ans = 1
    for i in range(n):
        arr.append(list(map(int, input().split())))
    l, r = 2, min(n, m)
    while l <= r:
        mid = (l + r) // 2
        if poss(n, m, arr, mid):
            l = mid + 1
            ans = mid
        else:
            r = mid - 1
    print(ans)

for _ in range(int(input())):
    solve()


    