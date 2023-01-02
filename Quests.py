import sys
input = lambda: sys.stdin.readline().rstrip("\n\r")

def solve():
    n, c, d = map(int, input().split())    
    a = list(map(int, input().split()))
    a.sort(reverse = True)
        
    if a[0] * d < c:
        print('Impossible')
        return
    
    l, r = 0, mx
    ans = 0
    while l <= r:
        m = (l + r) // 2
        #print(l, r, m)
        arr = [0] * d
        for i in range(n):
            if a[i] == 0:
                break
            for j in range(i, d, m + 1):
                if arr[j] != 0:
                    break
                else:
                    arr[j] = a[i]
        #print(arr)
        sm = sum(arr)
        if sm >= c:
            ans = m
            l = m + 1
        else:
            r = m - 1
        
    if ans >= d:
        print('Infinity')
    else:
        print(ans)

mx = int(10E5)
for _ in range(int(input())):
    solve()

    