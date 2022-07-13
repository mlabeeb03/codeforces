def solve():
    n = int(input())
    #n, m, x = map(int, input().split())    
    a = list(map(int, input().split())) 
    #a = list(map(str, input())) 
    
    s = sum(a)
    arr = [0, 0]
    for i in range(n):
        arr[i % 2] += a[i] - 1
    for i in range(2):
        if 2 * arr[i] > s:
            continue
        for j in range(n):
            if j % 2 == i:
                a[j] = 1
        break
    print(*a)
    
        
for _ in range(int(input())):
    solve()

    