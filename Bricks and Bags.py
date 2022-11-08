import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")

def solve():
    n = int(input())   
    a = list(map(int, input().split()))
    a.sort()
    
    ans=0
    for i in range(0,n-2):
        ans=max(ans,a[n-1]+a[i+1]-2*a[i])
    for j in range(n-1,1,-1):
        ans=max(ans,2*a[j]-a[0]-a[j-1])
    print(ans)
                
for _ in range(int(input())):
    solve()

    