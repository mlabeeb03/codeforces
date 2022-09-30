import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")

def solve():
    #n = int(input())
    ln, k, beauty, sm = map(int, input().split())    
    #a = list(map(int, input().split()))
    
    x = k * beauty
    sm -= x
    if sm < 0:
        print(-1)
        return
    x += min(k - 1, sm)
    sm -= min(k - 1, sm)
    ans = [0] * ln
    ans[0] = x
    for i in range(1, ln):
        if sm < k - 1:
            ans[i] = sm
            sm = 0
            break
        else:
            ans[i] = k - 1
            sm -= (k - 1)
    if sm == 0:
        print(*ans)
    else:
        print(-1)
        return

for _ in range(int(input())):
    solve()

    