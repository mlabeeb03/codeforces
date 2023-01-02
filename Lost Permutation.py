import sys
input = lambda: sys.stdin.readline().rstrip("\n\r")

def solve():
    #n = int(input())
    m, s = map(int, input().split())
    a = list(map(int, input().split()))
    st = set(a)
    for i in range(1, max(a)):
        if i not in st:
            s -= i
    if s == 0:
        print('YES')
        return
    x = max(a) + 1
    while s > 0:
        s -= x
        x += 1
    if s == 0:
        print('YES')
    else:
        print('NO')
        
    
    

    

for _ in range(int(input())):
    solve()

    