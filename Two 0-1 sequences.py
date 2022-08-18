import sys
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().strip()))
    b = list(map(int, input().strip()))
    
    a.reverse()
    b.reverse()
    
    for i in range(m - 1):
        if a[i] != b[i]:
            print('NO')
            return
    x = b[m - 1]
    for i in range(m - 1, n):
        if a[i] == x:
            print('YES')
            return
    print('NO')
            
for _ in range(int(input())):
    solve()

    