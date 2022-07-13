def solve():
    #n = int(input())
    n, m = map(int, input().split())    
    #a = list(map(int, input().split())) 
    #a = list(map(str, input())) 
    x = '1 0'
    y = '0 1'
    r1 = []
    r2 = []
    for i in range(m // 2):
        if i % 2 == 0:
            r1.append(x)
            r2.append(y)
        else:
            r1.append(y)
            r2.append(x)
          
    print(*r1)
    i = 1
    while True:
        print(*r2)
        i += 1
        if i == n:
            break
        print(*r2)
        i += 1
        if i == n:
            break
        print(*r1)
        i += 1
        if i == n:
            break
        print(*r1)
        i += 1
        if i == n:
            break

for _ in range(int(input())):
    solve()

    