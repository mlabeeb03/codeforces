def solve():
    n, c = map(str, input().split())
    n = int(n)
    a = list(input())
    if a.count(c) == n:
        print(0)
        return
    for i in range(n // 2, n):
        if a[i] == c:
            print(1)
            print(i + 1)
            return
    print(2)
    print(n, n - 1)

for _ in range(int(input())):
    solve()
    
        
        
        

    