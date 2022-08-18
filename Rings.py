#import sys
#input = sys.stdin.readline

def solve():
    n = int(input())
    #n, k = map(int, input().split())
    #a = list(map(int, input().split()))
    a = list(map(int, input()))
    
    rs = rind = 0    
    c = (n // 2) - 1
    for i in range(c + 1, n):
        if a[i] == 0:
            rs = 1
            rind = i + 1
    if rs == 1:
        print(1, rind, 1, rind - 1)
        return
    
    ls = lind = 0
    for i in range(c + 1):
        if a[i] == 0:
            ls = 1
            lind = i + 1
            break
    if ls == 1:
        print(lind, n, lind + 1, n)   
        return
    
    print(1, n - 1, 2, n)
    
for _ in range(int(input())):
    solve()

    