import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a[::2] = sorted(a[::2])
    a[1::2] = sorted(a[1::2])
    if a == sorted(a):
        print('YES')
        return
    print('NO')
    
for _ in range(int(input())):
    solve()

    