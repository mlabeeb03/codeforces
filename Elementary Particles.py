for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    x = [[] for _ in range(150001)]
    
    m = n+1
    
    for i in range(n):
        x[a[i]].append(i)
    
    for row in x:
        for e in range(len(row)-1):
            if row[e+1]-row[e] < m:
                m = row[e+1]-row[e]
    print(n-m)
                
        
    

    