import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")
 
def solve():
    n = int(input())
    a = list(map(int, input().split()))
    arr = 0
    for i in a:
        while i > 0 and i % 2 == 0:
            i //= 2
            arr += 1
    #print(arr)
    if arr >= n:
        print(0)
        return
    
    ind = []
    for i in range(1, n + 1):
        x = 0
        while i > 0 and i % 2 == 0:
            i //= 2
            x += 1
        ind.append(x)
    #print(ind)
        
    if arr + sum(ind) < n:
        print(-1)
        return
    
    ind.sort()
    ans = 0
    sm = arr + sum(ind)
    #print(sm)
    for i in ind:
        if sm - i >= n:
            sm -= i
            ans += 1
    print(n - ans)
    
                                   
for _ in range(int(input())):
    solve()