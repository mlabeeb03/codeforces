import sys
input = lambda: sys.stdin.readline().rstrip("\n\r")

def solve(): 
    n = int(input())
    
    pows = ((n * (n + 1) * (2 * n + 1)) // 6) - 1
    
    sub = (n * (n + 1)) // 2 - 1
    
    add = pows - sub
    
    ans = (pows + add)  + 1
    
    ans *= 2022
    ans %= 1000000007
    print(ans)

for _ in range(int(input())):
    solve()