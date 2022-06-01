def solve():
    n = int(input())
    a = list(map(int, input().split()))
    g = 1
    a.sort()
    i = 0
    while i < n:
        if a[i] <= g:
            g += 1
            i += 1
        else:
            mx = a[i]
            og = g
            while mx > g:
                i += 1
                if i == n:
                    g = og
                    break
                g += 1
                if a[i] > mx:
                    mx = a[i]
    print(g)
    

for __ in range(int(input())):
    solve()
                
    
    