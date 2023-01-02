import sys
input = lambda: sys.stdin.readline().rstrip("\n\r")

def solve():
    n = int(input())
    #n, k = map(int, input().split())
    #a = list(map(int, input().split()))
    
    print(n // 2 + (n % 2 != 0))

for _ in range(int(input())):
    solve()

    