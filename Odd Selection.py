def solve():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    
    e = 0
    o = 0
    
    for i in a:
        if i % 2 == 0:
            e += 1
        else:
            o += 1
            
    if o == 0:
        print('No')
        return
    if e == 0 and x % 2 == 0:
        print('No')
        return
    if e >= x:
        print('Yes')
        return
    
    if o % 2 == 1:
        if o + e >= x:
            print('Yes')
            return
    else:
        if (o - 1) + e >= x:
            print('Yes')
            return
    print('No')
    

for _ in range(int(input())):
    solve()
    
