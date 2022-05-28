for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    if a[0] != n and a[-1] != n:
        print(-1)
    else:
        for i in range(n-1, -1, -1):
            print(a[i], end = " ")
        print()
    
    
    

    