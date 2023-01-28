import sys
input = lambda: sys.stdin.readline().rstrip("\n\r")

def pos(a, x):
    aind = 0
    xind = 0
    while aind < len(a) and xind < len(x):
        if a[aind] == x[xind]:
            xind += 1
        aind += 1
    if xind == len(x):
        return True
    else:
        return False

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    l = 0
    r = ans = n // 2
    while l <= r:
        m = (l + r) // 2
        #print('here', m, m + 1, n - m + 1)
        x = [i for i in range(m + 1, n - m + 1)]
        #print(x)
        if pos(a, x):
            ans = m
            r = m - 1
            #print('hua')
        else:
            l = m + 1
            #print('not')
    print(ans)
    
for _ in range(int(input())):
    solve()