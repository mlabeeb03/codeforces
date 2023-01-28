import sys
input = lambda: sys.stdin.readline().rstrip("\n\r")

def solve():
    n = int(input())
    #n, m = list(map(int, input().split()))
    #a = list(map(int, input().split()))
    
    if n == 2:
        print(-1)
    else:
        print(n - 1)
    

for _ in range(int(input())):
    solve()