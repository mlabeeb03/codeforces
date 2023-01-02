import sys
input = lambda: sys.stdin.readline().rstrip("\n\r")

def solve():
    #n = int(input())
    #a, x = map(int, input().split())    
    a = list(map(int, input().split()))
    a.sort()
    print(a[1])
    
    

for _ in range(int(input())):
    solve()

    