import sys
input = lambda: sys.stdin.readline().rstrip("\n\r")

def solve():
    #n = int(input())
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))

    req = 1   
    for i in range(n):
        if a[i] == req:
            req += 1
            
    num = n - req + 1
    print(num // k + (num % k != 0))
    
for _ in range(int(input())):
    solve()