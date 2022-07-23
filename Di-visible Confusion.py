import sys
input = sys.stdin.readline
 
def solve():
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        fine = 0
        for j in range(2, i + 3):
            if a[i] % j != 0:
                fine = 1
                break
        if fine == 0:
            print('NO')
            return
    print('YES')

for _ in range(int(input())):
    solve()