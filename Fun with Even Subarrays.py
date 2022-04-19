for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    if len(set(a)) == 1:
        print(0)
    else:
        ans = 0
        x = 1
        a.reverse()
        
        while(x < n):
            if a[x] == a[0]:
                x += 1
                continue
            ans += 1
            x *= 2
        
        print(ans)
                
        
    

    