import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")
import math
def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    
    arr = a[:k]
    c = arr.count(arr[-1])
    d = a.count(arr[-1])
    
    print(math.comb(d, c) % num)
    
    
num = int(1E9 + 7)         
for _ in range(int(input())):
    solve()