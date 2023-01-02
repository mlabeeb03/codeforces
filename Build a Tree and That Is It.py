import sys
input = lambda: sys.stdin.readline().rstrip("\n\r")

def solve():
    n, d12, d23, d31 = list(map(int, input().split()))
    
    if (d12 + d23 + d31) % 2 or (d12 + d23 + d31) > 2 * (n - 1):
        print('NO')
    elif d12 + d23 < d31:
        print('NO')
    elif d12 + d31 < d23:
        print('NO')
    elif d23 + d31 < d12:
        print('NO')
    else:
        print('YES')
        d1 = (d12 + d31 - d23) // 2
        d2 = (d12 + d23 - d31) // 2
        d3 = (d23 + d31 - d12) // 2
        tmp = 4
        if d1 == 0: root = 1
        elif d2 == 0: root = 2
        elif d3 == 0: root = 3
        else:
            tmp = 5
            root = 4
        if d1 == 1:
            print(root, 1)
        elif d1 > 1:
            print(root, tmp)
            for i in range(d1 - 2):
                print(tmp, tmp + 1)
                tmp += 1
            print(tmp, 1)
            tmp += 1
        if d2 == 1:
            print(root, 2)
        elif d2 > 1:
            print(root, tmp)
            for i in range(d2 - 2):
                print(tmp, tmp + 1)
                tmp += 1
            print(tmp, 2)
            tmp += 1
        if d3 == 1:
            print(root, 3)
        elif d3 > 1:
            print(root, tmp)
            for i in range(d3 - 2):
                print(tmp, tmp + 1)
                tmp += 1
            print(tmp, 3)
            tmp += 1
        while tmp <= n:
            print(tmp - 1, tmp)
            tmp += 1
        
for _ in range(int(input())):
    solve()

    