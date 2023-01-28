import sys
input = lambda: sys.stdin.readline().rstrip("\n\r")
from collections import deque

def solve():
    n = int(input())
    #n, m = list(map(int, input().split()))
    #a = list(map(int, input().split()))
    a = deque([i for i in range(1, n**2 + 1)])
    #print(a)
    arr = []
    while a:   
        arr.append(a.popleft())
        try:
            arr.append(a.pop())
        except:
            pass
        
    for i in range(n):
        x = arr[i*n:(i + 1) * n]
        if i % 2 == 1:
            x.reverse()
        print(*x)

for _ in range(int(input())):
    solve()