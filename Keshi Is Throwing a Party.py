import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")

def solve():
    n = int(input())
    arr = []
    for i in range(1, n + 1):
        a, p = map(int, input().split())
        arr.append([(min(p, i - 1)), (min(n - i, a))])

    ans = 1
    l = 0
    r = n
    while l <= r:
        m = (l + r) // 2
        taken = 0
        required = m
        for i in range(n):
            if taken > arr[i][0]:
                continue
            elif required - 1 > arr[i][1]:
                continue
            else:
                taken += 1
                required -= 1
        if required < 1:
            ans = max(ans, m)
            l = m + 1
        else:
            r = m - 1

    print(ans) 
      
for _ in range(int(input())):
    solve()