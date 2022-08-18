import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")
 
def solve():
    n = int(input())
    #n, k = map(int, input().split())  
    #a = list(map(int, input().split()))
    ans = []
    if n % 2 == 1:
        ans.append(1)
        for i in range(3, n + 1, 2):
            ans.append(i)
            ans.append(i - 1)
    else:
        for i in range(2, n + 1, 2):
            ans.append(i)
            ans.append(i - 1)
    print(*ans)
        
for _ in range(int(input())):
    solve()