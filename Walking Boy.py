import sys
input = lambda: sys.stdin.readline().rstrip("\n\r")
#file = open('inp.txt', 'r') ; input = lambda: file.readline().rstrip("\n\r")

def solve():
    n = int(input()) + 2
    a = [0] + list(map(int, input().split())) + [1440]
    t = 0
    for i in range(1, n):
        t += (a[i] - a[i - 1]) // 120
    print('Yes' if t >= 2 else 'No')

    
for _ in range(int(input())):
    solve()