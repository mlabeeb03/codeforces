import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")
 
def solve():
    n = int(input())
    #n, m = map(int, input().split())
    d = list(map(int, input().split()))
    
    a = d[:]
    for i in range(1, n):
        a[i] = d[i] + a[i - 1]
        for j in range(0, a[i]):
            if abs(j - a[i - 1]) == d[i]:
                print(-1)
                return

    print(*a)
        
for _ in range(int(input())):
    solve()