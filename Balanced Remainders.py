for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    
    lst = [0,0,0]
    ans = 0
    
    for i in a:
        lst[i%3] += 1
        
    while lst[0] != lst[1] or lst[1] != lst[2]:
        if lst[0] >= lst[1] and lst[0] >= lst[2]:
            lst[0] -= 1
            lst[1] += 1
        elif lst[1] >= lst[0] and lst[1] >= lst[2]:
            lst[1] -= 1
            lst[2] += 1
        elif lst[2] >= lst[0] and lst[2] >= lst[1]:
            lst[2] -= 1
            lst[0] += 1
        ans += 1
    
    print(ans)


    