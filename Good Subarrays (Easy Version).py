import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    i = j = old = 0
    while i < n and j < n:
        while j < n and a[j] + i > j:
            j += 1
        s = j - i
        ans += (s * (s + 1) // 2) - s
        if old > 0:
            s = old - i
            ans -= (s * (s + 1) // 2) - s
        old = j
        if j >= n:
            break
        i = j - (a[j] - 1)
    print(ans + n)
    
    
for _ in range(int(input())):       
    solve()