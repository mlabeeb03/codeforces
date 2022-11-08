import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")

def solve():
    #n, m = map(int, input().split())
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = 0
    i = 0
    j = n - 1
    while i < j:
        if b[i] > b[j]:
            ans += a[j]
            a[j - 1] += b[j]
            j -= 1
        else:
            ans += a[i]
            a[i + 1] += b[i]
            i += 1
    ans += a[i]
    print(ans)
    
for _ in range(int(input())):
    solve()

    