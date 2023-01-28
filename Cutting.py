import sys
input = lambda: sys.stdin.readline().rstrip("\n\r")

def solve():
    n, b = list(map(int, input().split()))
    a = list(map(int, input().split()))
    
    e = 0
    o = 0
    
    cts = []
    
    for i in range(n - 1):
        if a[i] % 2 == 0:
            e += 1
        else:
            o += 1
            
        if e == o:
            cts.append(abs(a[i] - a[i + 1]))
            
    cts.sort(reverse = True)
    ans = 0
    while cts:
        x = cts.pop()
        if x <= b:
            ans += 1
            b -= x
        else:
            break
        
    print(ans)

for _ in range(1):
    solve()