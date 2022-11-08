import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")
from collections import deque
def solve():
    n = int(input())
    if n < 4:
        print(-1)
        return
    d = deque([2, 4, 1, 3])
    for i in range(5, n + 1, 2):
        d.append(i)
        if i != n:
            d.appendleft(i + 1)
    print(*d)
                                   
for _ in range(int(input())):
    solve()
