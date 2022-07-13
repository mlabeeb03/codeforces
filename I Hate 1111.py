def solve():
    n = int(input())
    #n, W = map(int, input().split())    
    #a = list(map(int, input().split())) 
    
    if n > 1099:
        print('YES')
        return
    while n >= 0:
        if n % 11 == 0:
            print('YES')
            return
        n -= 111
    print('NO')
         
for _ in range(int(input())):
    solve()

    