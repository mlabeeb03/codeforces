def solve():
    n = int(input())
    a = list(map(int, input().split()))
    #n, k = map(int, input().split())
    
    if len(set(a)) == 1:
        print('NO')
        return
    print('YES')
    x = a[0]
    for i in range(n):
        if a[i] != x:
            print(1, i + 1)
    y = -1
    for i in range(n):
        if a[i] != x:
            y = i + 1
            break
    
    for i in range(1, n):
        if a[i] == x:
            print(min(y, i + 1), max(y, i + 1))
    
    
for t in range(int(input())):
	solve()
