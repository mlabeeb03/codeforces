import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")
 
def solve():
    n, k = map(int, input().split())  
    a = list(map(int, input().split()))
    ans = 0
    for i in range(k):
        if a[i] > k:
            ans += 1
    print(ans)
        
for _ in range(int(input())):
    solve()