import sys
input = lambda: sys.stdin.readline().rstrip("\n\r")

def solve():
    n = int(input())    
    #a = list(map(str, input())) 
    
    if n % 2 == 0:
        print('YES')
        for i in range(n//2):
            print(-1, 1, end = ' ')
        print()
    else:
        if n == 3:
            print('NO')
        else:
            print('YES')
            m = n // 2
            for i in range(n//2):
                print(m - 1, -m, end = ' ')
            print(m - 1)

for _ in range(int(input())):
    solve()

    