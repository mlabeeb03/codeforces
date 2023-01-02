import sys
input = lambda: sys.stdin.readline().rstrip("\n\r")
from collections import deque

def solve():
    n = int(input())  
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    ref = [i for i in range(int(5 * 10 ** 5) + 1)]
    ans = deque([])
    for i in range(n - 1, -1, -1):
        if a[i][0] == 2:
            ref[a[i][1]] = ref[a[i][2]]
        else:
            ans.appendleft(ref[a[i][1]])   
    
    print(*ans)

for _ in range(1):
    solve()


    