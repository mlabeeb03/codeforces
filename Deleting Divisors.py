import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")

def solve():
    n = int(input())
    #n, c, q = map(int, input().split()) 
    if n % 2 == 1:
        print('Bob')
        return
    cnt = 0
    while n % 2 == 0:
        cnt += 1
        n //= 2
    if n > 1:
        print('Alice')
    elif cnt % 2 == 0:
        print('Alice')
    else:
        print('Bob')
    
for _ in range(int(input())):
    solve()

    