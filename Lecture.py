import sys
input = lambda: sys.stdin.readline().rstrip("\n\r")

def solve():
    n, m = list(map(int, input().split()))
    dic = {}
    for i in range(m):
        x, y = list(map(str, input().split()))
        if len(x) <= len(y):
            dic[x] = x
            dic[y] = x
        else:
            dic[x] = y
            dic[y] = y
    a = list(map(str, input().split()))
    for i in a:
        print(dic[i], end = ' ')

for _ in range(1):
    solve()