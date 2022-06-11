def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    dif = 1000000000
    for i in range(n):
        if b[i] > 0:
            dif = a[i] - b[i]
            
    if dif < 0:
        print('NO')
        return
    
    for i in range(n):
        new = a[i] - b[i]
        if b[i] > 0:
            if new != dif:
                print('NO')
                return
        else:
            if new > dif:
                print('NO')
                return
    print('YES')
        

for _ in range(int(input())):
    solve()

    