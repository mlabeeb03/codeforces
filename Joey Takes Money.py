import sys
input = lambda: sys.stdin.readline().rstrip("\n\r")

def solve(): 
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(1, n):
        a[0] = a[0] * a[i]
        a[i] = 1
    print(2022 * sum(a))

for _ in range(int(input())):
    solve()


    