import sys
input = lambda: sys.stdin.readline().rstrip("\n\r")

def solve(): 
    n, m = list(map(int, input().split()))
    g = [set() for i in range(n + 1)]
    ln = [0] * (n + 1)
    for i in range(m):
        x, y = list(map(int, input().split()))
        g[x].add(y)
        g[y].add(x)
        ln[x] += 1
        ln[y] += 1
        
    if ln.count(1) == 2 and ln.count(2) == n - 2:
        print('bus topology')
    elif ln.count(2) == n:
        print('ring topology')
    elif ln.count(1) == n - 1:
        print('star topology')
    else:
        print('unknown topology')
        
for _ in range(1):
    solve()


    