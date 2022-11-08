import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")

def solve():
    #n = int(input())
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    if 1 in a:
        print('YES')
    else:
        print('NO')
                                   
for _ in range(int(input())):
    solve()
