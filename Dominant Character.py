def solve():
    n = int(input())
    #n, W = map(int, input().split())    
    #a = list(map(int, input().split())) 
    a = list(map(str, input())) 
    
    for i in range(n - 1):
        if a[i] == 'a' and a[i + 1] == 'a':
            print(2)
            return
    for i in range(n - 2):
        if a[i] == 'a' and a[i + 2] == 'a':
            print(3)
            return
    for i in range(n - 3):
        if a[i] == 'a' and a[i + 3] == 'a' and a[i + 1] != a[i + 2]:
            print(4)
            return
    for i in range(n - 6):
        if a[i] == 'a' and a[i + 3] == 'a'and a[i + 6] == 'a' and a[i + 1] != a[i + 4] and a[i + 2] != a[i + 5]:
            print(7)
            return
    print(-1)
            
for _ in range(int(input())):
    solve()

    