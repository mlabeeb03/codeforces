import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    arr = []
    for i in range(n):
        arr.append([abs(a[i]), i])
    arr.sort()
    b = [None] * n
    done = 0
    for i in range(n - 1):
        if b[arr[i][1]] is not None:
            continue
        x = a[arr[i][1]]
        y = a[arr[i + 1][1]]
        if abs(x) == abs(y):
            done += 2
            if abs(x + y) < abs(x) + abs(y):
                b[arr[i][1]], b[arr[i + 1][1]] = 1, 1
            else:
                b[arr[i][1]], b[arr[i + 1][1]] = 1, -1

    if done == n:
        print(*b)
        return
    if done == n - 1:
        for i in range(n - 1):
            if arr[i][0] == arr[i + 1][0]:
                b[arr[i][1]] = None
                b[arr[i + 1][1]] = None
                break
            
    mn = 100000
    ind = 0
    for i in range(n):
        if abs(a[i]) < mn and b[i] is None:
            mn = abs(a[i])
            ind = i
    sm = 0
    for i in range(n):
        if b[i] is None:
            sm += abs(a[i])
    sm -= abs(a[ind])
    pa = abs(a[ind])
    pn = pa * -1
    for i in range(n):
        if b[i] is None:
            if a[i] > 0:
                b[i] = pa
            else:
                b[i] = pn
    if a[ind] > 0:
        b[ind] = sm * -1
    else:
        b[ind] = sm
    print(*b)

for _ in range(int(input())):
    solve()