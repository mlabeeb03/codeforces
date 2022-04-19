tcs = int(input())
for _ in range(tcs):
    n = int(input())
    a = list(map(int, input().split()))
    
    a.sort()
    
    if a[n-1] <= 0:
        print(n)        
    else:  
        flag = 0
        pi = 0
        while(a[pi] <= 0):
            pi += 1
        
        for i in range(pi):
            x = a[i] - a[i+1]
            if abs(x) < a[pi]:
                flag = 1
                
        print(pi+1 if flag == 0 else pi)

    