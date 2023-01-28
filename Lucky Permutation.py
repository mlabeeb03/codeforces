import sys
input = lambda: sys.stdin.readline().rstrip("\n\r")
    
def solve():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        a[i] -= 1
    
    ind, ans = 1, 0
    comp = [0] * n
    for i in range(n):
        if comp[i]:
            continue
        v = i
        while comp[v] == 0:
            comp[v] = ind
            v = a[v]
            ans += 1
        ind += 1
        ans -= 1
        
    for i in range(n - 1):
        if comp[i] == comp[i + 1]:
            print(ans - 1)
            return
    print(ans + 1)
    
for _ in range(int(input())):
    solve()