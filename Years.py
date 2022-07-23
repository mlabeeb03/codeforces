import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    a = []
    for i in range(n):
        x, y = map(int, input().split())
        a.append([x, 1])
        a.append([y, -1])
    a.sort()
    
    year = 0
    count = 0
    ans = 0
    for i in range(2 * n):
        count += a[i][1]
        if count > ans:
            year = a[i][0]
            ans = count
    print(year, ans)
         
for _ in range(1):
    solve()