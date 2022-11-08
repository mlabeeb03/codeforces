import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    a = b = 0
    for i in arr:
        if i % 2 == 0:
            a += 1
        else:
            b += 1
    if b % 4 == 2:
        print('Bob')
    elif b % 4 == 3:
        print('Alice')
    elif b % 4 == 0:
        print('Alice')
    elif a % 2 == 1:
        print('Alice')
    else:
        print('Bob')
        
for _ in range(int(input())):
    solve()