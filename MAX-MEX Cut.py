for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input()))
    b = list(map(int, input()))
    
    ans = 0
    i = 0
    while i < n-1:
        if a[i] != b[i]:
            ans += 2
            i += 1
        else:
            if a[i] == 1:
                if a[i+1] == 0 and b[i+1] == 0:
                    ans += 2
                    i += 2
                else:
                    i += 1
            else:
                if a[i+1] == 1 and b[i+1] == 1:
                    ans += 2
                    i += 2
                else:
                    ans += 1
                    i += 1
    if i == n-1:
        if a[n-1] != b[n-1]:
            ans += 2
        elif a[n-1] == 0:
            ans += 1
        else:
            ans += 0
    
    print(ans)


    