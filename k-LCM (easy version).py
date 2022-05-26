for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    if n%3 == 0:
        print(int(n/3),int(n/3),int(n/3))
    else:
        if n%2 == 0:
            if (n/2)%2 == 0:
                print(int(n/2),int(n/4),int(n/4))
            else:
                print(int(n/2)-1,int(n/2)-1,2)
        else:
            print(int(n/2),int(n/2),1)


