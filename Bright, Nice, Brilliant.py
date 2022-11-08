import sys
input = lambda: sys.stdin.readline().rstrip("\r\t")

def solve():
    n = int(input())
    print(1)
    n -= 1
    if n > 0:
        print(1, 1)
        n -= 1
    for i in range(n):
        print(1, end = ' ')
        print('0 ' * (i + 1), end = '')
        print(1)
       
for _ in range(int(input())):
    solve()
    
    

    