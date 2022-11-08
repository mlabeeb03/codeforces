import sys
input = lambda: sys.stdin.readline().rstrip("\r\t")

def solve():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    arr = [0] * (x + 1)
    for i in a:
        arr[i] += 1
    
    for i in range(1, x):
        if arr[i] % (i + 1) > 0:
            print('No')
            return
        arr[i + 1] += arr[i] // (i + 1)
    print('Yes')
       
for _ in range(1):
    solve()
    
    

    