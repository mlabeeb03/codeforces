def solve():
    m = int(input())
    #n, l, r = map(int, input().split())
    a = [None, None]
    a[0] = list(map(int, input().split()))
    a[1] = list(map(int, input().split()))
    
    b = a[:]
    ans = None
    for i in range(1, m):
        b[0][i] += b[0][i-1]
        b[1][i] += b[1][i-1]
    for i in range(m):
        s = None
        if i == 0:
            s = b[0][m - 1] - b[0][0]
        elif i == m - 1:
            s = b[1][m - 2]
        else:
            s = max(b[0][m-1] - b[0][i], b[1][i-1])
        if ans == None:
            ans = s
        else:
            ans = min(ans, s)
    print(ans)

for __ in range(int(input())):
    solve()