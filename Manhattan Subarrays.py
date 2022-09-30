import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")

def check(x, y, z):
    if (x <= y and y <= z) or (x >= y and y >= z):
        return 0
    return 1
def solve():
    n = int(input())
    #n, m = map(int, input().split())    
    a = list(map(int, input().split()))
    
    ans = n + (n - 1)
    
    for i in range(2, n):
        x, y, z = a[i - 2], a[i - 1], a[i]
        ans += check(x, y, z)        
    
    for i in range(3, n):
        w, x, y, z = a[i - 3], a[i - 2], a[i - 1], a[i]
        if check(w, x, y) and check(w, x, z) and check(w, y, z) and check(x, y, z):
            ans += 1
    print(ans)

for _ in range(int(input())):
    solve()

    