import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    l = 1
    r = n 
    while l <= r:
        m = (l + r) // 2
        i = n - 1
        j = 0
        taken = 0
        cantake = m     
        while i >= j:
            while i > -1 and a[i] > cantake:
                i -= 1
            if i == -1 or i < j:
                break
            else:
                taken += 1
                cantake -= 1
                i -= 1
            j += 1
        if taken == m:
            ans = max(ans, m)
            l = m + 1
        else:
            r = m - 1
            
    print(ans)
    
for _ in range(int(input())):
    solve()