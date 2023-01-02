import sys
input = lambda: sys.stdin.readline().rstrip("\n\r")


def solve():  
    n, m = list(map(int, input().split()))
    arr = []
    for i in range(n):
        arr.append(list(map(int, input().split())))
        
    for i in range(n):
        if i % 2 == 0:
            for j in range(0, m, 2):
                if arr[i][j] % 2 == 1:
                    arr[i][j] += 1
            for j in range(1, m, 2):
                if arr[i][j] % 2 != 1:
                    arr[i][j] += 1
        else:
            for j in range(0, m, 2):
                if arr[i][j] % 2 != 1:
                    arr[i][j] += 1
            for j in range(1, m, 2):
                if arr[i][j] % 2 == 1:
                    arr[i][j] += 1
    for i in arr:
        print(*i)

for _ in range(int(input())):
    solve()


    