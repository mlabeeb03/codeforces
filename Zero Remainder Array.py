import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")
def solve():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    dic = {}
    for i in range(n):
        if arr[i] % k != 0:
            x = k - arr[i] % k
            if x not in dic:
                arr[i] = x
                dic[x] = 1
            else:
                arr[i] = x + k * dic[x]
                dic[x] += 1
        else:
            arr[i] = 0
    if max(arr) > 0:
        print(max(arr) + 1)
    else:
        print(0)
            
for _ in range(int(input())):
    solve()