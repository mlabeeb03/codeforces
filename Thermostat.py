import sys
input = lambda: sys.stdin.readline().rstrip("\n\r")

def solve():
    #n = int(input())
    l, r, x = map(int, input().split())
    a, b = map(int, input().split())
    #a = list(map(int, input().split()))
    
    if a == b:
        print(0)
        return
    if abs(a - b) >= x:
        print(1)
        return
    if a - l >= x and b - l >= x:
        print(2)
        return
    if r - a >= x and r - b >= x:
        print(2)
        return
    if r - a >= x and r - l >= x and b - l >= x:
        print(3)
        return
    if a - l >= x and r - l >= x and r - b >= x:
        print(3)
        return
    print(-1)

for _ in range(int(input())):
    solve()

    