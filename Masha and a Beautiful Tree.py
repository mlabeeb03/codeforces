import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")
import math
def solve():
    n = int(input())
    a = list(map(int, input().split()))
    steps = int(math.log(n, 2))
    ans = 0
    for i in range(steps):
        newarr = a[:]
        a = []
        for j in range(0, len(newarr) - 1, 2):
            if newarr[j + 1] == newarr[j] + 1:
                a.append(newarr[j + 1] // 2)
            elif newarr[j] == newarr[j + 1] + 1:
                a.append(newarr[j] // 2)
                ans += 1
            else:
                print(-1)
                return
    print(ans)
                                   
for _ in range(int(input())):
    solve()