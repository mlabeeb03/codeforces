import sys
input = sys.stdin.readline

import heapq as hq
def solve():
    n = int(input())
    a = list(map(int, input().split()))
    h = 0
    arr = []
    for i in range(n):
        h += a[i]
        hq.heappush(arr, a[i])
        while h < 0:
            h -= hq.heappop(arr)
    print(len(arr))
    
for _ in range(1):
    solve()