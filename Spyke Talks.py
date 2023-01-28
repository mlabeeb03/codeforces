import sys
input = lambda: sys.stdin.readline().rstrip("\n\r")
from collections import Counter

def solve():
    n = int(input())    
    a = Counter(list(map(int, input().split())))
    ans = 0
    for i in a.keys():
        if i == 0:
            continue
        if a[i] == 2:
            ans += 1
        if a[i] > 2:
            print(-1)
            return
    print(ans)

for _ in range(1):
    solve()

    