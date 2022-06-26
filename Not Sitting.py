def solve():
    #n = int(input())
    n, m = map(int, input().split())
    #a = list(map(int, input().split()))
    #a = list(map(int, input()))
    
    lst = []
    for i in range(n):
        for j in range(m):
            lst.append(max(i, n - i - 1) + max(j, m - j - 1))
    lst.sort()
    print(*lst[:n*m])
    
for __ in range(int(input())):
    solve()

   