import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")

def solve():
    #n = int(input())
    n, m = map(int, input().split())    
    #a = list(map(int, input().split()))
    
    if n == 1 and m == 1:
        print(0)
        return
    
    ans = 0
    ans += m - 1
    ans += n - 1
    ans += min(m, n)
    
    print(ans)

for _ in range(int(input())):
    solve()

    