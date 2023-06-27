import sys
try:
    file = open('inp.txt', 'r')
    input = lambda: file.readline().rstrip("\n\r")
except:
    input = lambda: sys.stdin.readline().rstrip("\n\r")

def solve():
    #n = int(input())
    #a, b, c= map(int, input().split())
    #a = list(map(int, input().split()))
    a = list(map(int, input().split()))
    if (a+b+c) % 3 != 0:
        print(-1)
        return
    else:
        fin = (a+b+c) // 3
        given = 0
        if a > fin:
            given += a - fin
        if b > fin:
            given += b - fin
        if c > fin:
            given += c - fin
        print(given)
    

for _ in range(int(input())):
    solve()
