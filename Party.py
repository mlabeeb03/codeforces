import sys
input = sys.stdin.readline
import math

def solve():
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    deg=[0]*n
    pairs=[]
    for i in range(m):
        x, y = map(int, input().split())
        pairs.append([x - 1, y - 1])
        deg[x - 1] += 1
        deg[y - 1] += 1
    ans = math.inf
    for i in range(n):
        if(deg[i]%2!=0):
            ans=min(ans,a[i])
    for i in range(m):
        x = pairs[i][0]
        y = pairs[i][1]
        if deg[x]%2==0 and deg[y]%2==0:
            ans=min(ans,a[x]+a[y])
    if(m%2==0):
        print(0)
    else:
        print(ans)

for _ in range(int(input())):
    solve()

    