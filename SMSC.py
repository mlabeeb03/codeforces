import sys
input = lambda: sys.stdin.readline().rstrip("\n\r")

def solve():
    n = int(input())    
    a = [list(map(int, input().split())) for i in range(n)]
    curr = top = a[0][1]
    
    for i in range(1, n):
        dist = a[i][0] - a[i - 1][0]
        curr = max(0, curr - dist)
        curr += a[i][1]
        top = max(curr, top)
        
    time = a[-1][0] + curr
    
    print(time, top)

for _ in range(1):
    solve()

    