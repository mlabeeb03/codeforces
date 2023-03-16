import sys
input = lambda: sys.stdin.readline().rstrip("\n\r")

def solve():
    n = int(input())
    #n, k = map(int, input().split())
    a = list(map(int, input().split()))
    tot = a.count(2)
    if tot % 2 == 1:
        print(-1)
        return
    loc = 0
    for i in range(n):
        if a[i] == 2:
            loc += 1
        if loc == tot // 2:
            print(i + 1)
            return
    
    print(-1)

for _ in range(int(input())):
    solve()
    