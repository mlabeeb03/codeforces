import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")

def solve():
    #n = int(input())  
    n, m, sx, sy, d = list(map(int, input().split()))
    ans = (n - 1) + (m - 1)
    
    if (sx - 1) > d and (m - sy) > d:
        print(ans)
    elif (sy - 1) > d and (n - sx) > d:
        print(ans)
    else:
        print(-1)

for _ in range(int(input())):
    solve()

    
    

    