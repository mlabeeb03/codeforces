#import sys
#input = sys.stdin.readline

def solve():
    n = int(input())
    #n, k = map(int, input().split())
    #a = list(map(int, input().split()))
    ans = 0
    for i in range(3, n, 2):
        if i * i >= 2 * n + 1:
            break
        ans += 1
    print(ans)
    
for _ in range(int(input())):
    solve()

    