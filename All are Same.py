def find_gcd(x, y):
    while(y):
        x, y = y, x % y 
    return x

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    a = list(set(a))
    n = len(a)     
    a.sort()
     
    try:
        for i in range(1,n):
            a[i] = a[i] - a[0]
        
        g = a[1]
            
        for i in range(2,n):
            g = find_gcd(g, a[i])            
        print(g)
    except:
        print(-1)
    
    
    
    