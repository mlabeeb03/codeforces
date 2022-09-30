def solve():
    n, k = map(int, input().split())    
    if n == 4:
        if k == 0:
            print('0 3\n1 2')
        elif k == 1:
            print('0 2\n1 3')
        elif k == 2:
            print('0 1\n2 3')
        else:
            print(-1)
    else:
        if k == 0:
            for i in range(n//2):
                print(i, (n - 1) - i)
        elif k < n - 1:
            print(n - 1, k)
            if k < n//2:
                print(0, (n - 1) - k)
            else:
                print(0, k - ((k - n//2) * 2 + 1))
            for i in range(n//2):
                if i == 0 or (i == k and k < n//2) or (i == k - ((k - n//2) * 2 + 1) and k >= n//2):
                    continue
                print(i, (n - 1) - i)
        else:
            print(n - 1, k - 1)
            print(1, k - 2)
            print(2, 0)
            for i in range(3, n//2):
                print(i, (n - 1) - i)  

for _ in range(int(input())):
    solve()

    