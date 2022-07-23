def solve():
    n = int(input())  
    a = list(map(int, input().split()))
    
    s = 0
    for i in range(n):
        s = i
        if a[i] != 0:
            break
           
    sm = sum(a[:-1])
    sm += a[s:-1].count(0)
    print(sm)

for _ in range(int(input())):
    solve()

    