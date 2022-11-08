import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")

def solve():
    n = int(input())
    #n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    zi = []
    for i in range(n):
        if a[i] == 0:
            zi.append(i)
    l = len(zi)
    ans = 0
    for i in range(n):
        if l == 0:
            break
        if a[i] == 1 and i > zi[-1]:
            break
        if a[i] == 1 and i < zi[-1]:
            ans += 1
            l -= 1
            zi.pop()
    print(ans)
                                   
for _ in range(int(input())):
    solve()
