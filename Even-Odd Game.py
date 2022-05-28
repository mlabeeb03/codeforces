def solve():
    #n, k = map(int, input().split())
    n = int(input())
    a = list(map(int, input().split()))    
    a.sort()
    ascr = 0
    bscr = 0
    while a:
        x = a.pop()
        if x % 2 == 0:
            ascr += x
        if a:
            x = a.pop()
            if x % 2 == 1:
                bscr += x
    if ascr>bscr:
        print('Alice')
    elif bscr>ascr:
        print('Bob')
    else:
        print('Tie')

for _ in range(int(input())):
    solve()

    