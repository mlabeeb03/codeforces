import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")

def solve():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    if k == 1:
        print('Yes')
        return
    b = [None] * (k - 1)
    for i in range(k - 1):
        b[i] = arr[i + 1] - arr[i]
    if b != sorted(b):
        print('No')
        return
    if b[0] * (n - k + 1) < arr[0]: 
        print('No')
        return
    print('Yes')
        
for _ in range(int(input())):
    solve()