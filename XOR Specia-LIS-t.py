def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    x = False
    
    for i in range(n-1):
        if a[i] >= a[i+1]:
            x = True
            
    if n % 2 == 0 or x:
        print('YES')
    else:
        print('NO')
        
    
for __ in range(int(input())):   
    solve()
                
    
    