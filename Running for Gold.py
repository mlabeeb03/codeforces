import sys
input = sys.stdin.readline

def asupb(a, b):
    x = 0
    y = 0
    for i in range(5):
        if a[i] < b[i]:
            x += 1
        else:
            y += 1
    if x > y:
        return True
    return False

def solve():
    n = int(input())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    w = 0
    for i in range(1, n):
        if asupb(a[i], a[w]):
            w = i
    for i in range(n):
        if i != w:
            if asupb(a[i], a[w]):
                print(-1)
                return
    print(w + 1)
    
for _ in range(int(input())):
    solve()
    