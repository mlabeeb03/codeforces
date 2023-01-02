import sys
input = lambda: sys.stdin.readline().rstrip("\n\r")
from collections import Counter
def solve():
    n = int(input())
    #n, x = map(int, input().split())    
    a = list(map(str, input()))
    for i in range(n):
        a[i] = ord(a[i])
    x = max(a)
    print(x - 96)
    
    

for _ in range(int(input())):
    solve()

    