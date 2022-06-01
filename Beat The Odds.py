def solve():
    n = int(input())
    a = list(map(int, input().split()))
    enum = 0
    onum = 0
    for i in a:
        if i % 2 == 0:
            enum += 1
        else:
            onum += 1
    print(min(enum, onum))
    
for __ in range(int(input())):   
    solve()
                
    
    