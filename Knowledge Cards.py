import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")
import heapq as hq

def solve():
    n, m, k = map(int, input().split())    
    a = list(map(int, input().split()))
    arr = [i for i in range(1, k + 1)]
    t = n * m - 3
    hp = []
    for i in range(k):
        hq.heappush(hp, a[i] * -1)
        if len(hp) > t:
            print('tidak')
            return
        while hp and arr and hp[0] * -1 == arr[-1]:
            arr.pop()
            hq.heappop(hp)
        
    print('ya')

for _ in range(int(input())):
    solve()

    