import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")
import math
def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    x = arr[0]
    for i in range(1, n):
        x &= arr[i]
    count = arr.count(x)
    if count < 2:
        print(0)
        return
    print((count * (count - 1) * (math.factorial(n - 2))) % num)
    
num = int(1E9 + 7)         
for _ in range(int(input())):
    solve()