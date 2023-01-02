import sys
input = lambda: sys.stdin.readline().rstrip("\n\r")
import math

def solve():
    n = int(input())    
    a = list(map(int, input().split()))
    
    arr = [a[0]]
    for i in range(1, n):
        if a[i] != arr[-1]:
            arr.append(a[i])
    ln = len(arr)
    
    if ln == 1:
        print('YES')
        return
    
    ans = 0
    b = [math.inf] + arr + [math.inf]
    
    for i in range(1, ln + 1):
        if b[i] < b[i - 1] and b[i] < b[i + 1]:
            ans += 1
    
    if ans == 1:
        print('YES')
    else:
        print('NO')
    
    

for _ in range(int(input())):
    solve()

    