def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    
    arr = [False for i in range(n)]
    for i in range(n):
        while a[i] > n:
            a[i] //= 2
        while arr[a[i] - 1] is True and a[i] > 0:
            a[i] //= 2
        if a[i] == 0:
            print('NO')
            return
        arr[a[i] - 1] = True
    print('YES')
for t in range(int(input())):
	solve()