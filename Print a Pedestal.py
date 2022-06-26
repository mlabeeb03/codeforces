for _ in range(int(input())):
    n = int(input())
    n -= 6
    a = 2 + (n // 3)
    b = 3 + (n // 3)
    c = 1 + (n // 3)
    
    if n % 3 == 1:
        b += 1
    if n % 3 == 2:
        a += 1
        b += 1
    print(a, b, c)
    



