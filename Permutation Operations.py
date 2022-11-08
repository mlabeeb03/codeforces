import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")
 
def solve():
    n = int(input())
    a = list(map(int, input().split()))
    ans = [None] * (n + 1)
    rem = []
    req = []
    mx = a[0]
    for i in range(1, n):
        if a[i] < mx: 
            if ans[mx - a[i] + 1] is None:
                ans[mx - a[i] + 1] = i + 1
            else:
                req.append([mx - a[i] + 1, i + 1])
        else:
            mx = a[i]
    for i in range(1, n + 1):
        if ans[i] is None:
            rem.append(i)
    req.sort()
    remind = 0
    for i in range(len(req)):
        x = req[i][0]
        ind = req[i][1]
        while True:
            x -= rem[remind]
            ans[rem[remind]] = ind
            remind += 1
            if x < 1:
                break
    for i in range(1, n + 1):
        if ans[i] is None:
            ans[i] = n
    print(*ans[1:])
                                   
for _ in range(int(input())):
    solve()