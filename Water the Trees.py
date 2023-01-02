import sys
input = lambda: sys.stdin.readline().rstrip("\n\r")

def do(a, m):
    o = (m // 2) + (m % 2 > 0)
    t = m // 2
    for i in range(len(a)):
        if t >= a[i] // 2:
            t -= a[i] // 2
            a[i] %= 2
        else:
            a[i] -= t * 2
            t = 0
    for i in a:
        o -= i
    if o > -1:
        return True
    return False
                
def solve():
    n = int(input())    
    a = list(map(int, input().split()))
    mx = max(a)
    req1 = sorted([mx - i for i in a])
    req2 = sorted([mx - i + 1 for i in a])
    ans, l, r = mxnm, 0, mxnm
    while l <= r:
        m = (l + r) // 2
        if do(req1[:], m) or do(req2[:], m):
            ans = m
            r = m - 1
        else:
            l = m + 1
    print(ans)
        
mxnm = int(1 * 10E18)
for _ in range(int(input())):
    solve()

    