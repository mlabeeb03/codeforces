for _ in range(int(input())):
    a, b = map(int, input().split())
    xor = 0
    
    if a % 4 == 1:
        xor = a-1
    elif a % 4 == 2:
        xor = 1
    elif a % 4 == 3:
        xor = a
    else:
        xor = 0
        
    if xor == b:
        print(a)
    elif xor ^ b != a:
        print(a+1)
    else:
        print(a+2)
    
    

    