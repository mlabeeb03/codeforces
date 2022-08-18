import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    #r, c, k = map(int, input().split())    
    #a = list(map(int, input().split()))
    
    ans = [n]
    for i in range(1, n):
        ans.append(i)
    print(*ans)

for _ in range(int(input())):
    solve()

    