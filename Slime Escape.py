import sys
input = lambda: sys.stdin.readline().rstrip("\r\t")

def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    k -= 1
    l = k - 1
    r = k + 1
    curr = a[k]
    while l >= 0 and r <= n - 1:
        did = 0
        
        local = curr
        for i in range(l, -2, -1):
            if i == -1:
                print('YES')
                return
            local += a[i]
            if local < 0:
                break
            elif local > curr:
                curr = local
                l = i - 1
                did = 1
                
        local = curr
        for i in range(r, n + 1):
            if i == n:
                print('YES')
                return
            local += a[i]
            if local < 0:
                break
            elif local > curr:
                curr = local
                r = i + 1
                did = 1
                
        if did == 0:
            print('NO')
            return
    print('YES')
       
for _ in range(int(input())):
    solve()
    
    

    