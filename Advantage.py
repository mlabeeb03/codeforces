import sys
input = lambda: sys.stdin.readline().rstrip("\n\r")

def solve():
    n = int(input())   
    a = list(map(int, input().split()))
    
    mx = max(a)
    if a.count(mx) > 1:
        for i in range(n):
            print(a[i] - mx, end = ' ')
        print()
    else:
        smx = 0
        for i in range(n):
            if a[i] == mx:
                continue
            else:
                smx = max(smx, a[i])
        for i in range(n):
            if a[i] == mx:
                print(mx - smx, end = ' ')
            else:
                print(a[i] - mx, end = ' ')
        print()
    

for _ in range(int(input())):
    solve()

    