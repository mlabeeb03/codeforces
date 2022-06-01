for _ in range(int(input())):
    a, b = map(int, input().split())  
    
    ext = 0
    if b < 2:
        b = 2
        ext = 1
        
    ans = 30
    
    for i in range(b, b + 7):
        x = 0
        A = a
        while A:
            A //= i
            x += 1
        if x + (i - b) < ans:
            ans = x + (i - b)
    
    print(ans+ext)


    