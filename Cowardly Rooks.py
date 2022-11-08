import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")

def solve():
    n, m = map(int, input().split())
    #n = int(input())
    #lid = list(map(int, input()))
    #bok = list(map(int, input().split()))
    for i in range(m):
        x, y = map(int, input().split())
    if n == m:
        print('NO')
    else:
        print('YES')
    
for _ in range(int(input())):
    solve()

    