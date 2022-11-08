import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")

def solve():
    n, k, z = map(int, input().split())
    arr = list(map(int, input().split()))
    pre = arr[:]
    for i in range(1, n):
        pre[i] += pre[i - 1]
    ans = 0
    for i in range(1, n):
        if i > k:
            break
        sm = pre[i]
        moves = k - i
        #print(i, sm, moves)
        if moves == -1:
            break
        if z * 2 == moves:
            sm += (arr[i] + arr[i - 1]) * z
        elif z * 2 < moves:
            sm += (arr[i] + arr[i - 1]) * z
            moves -= z * 2
            sm += pre[i + moves] - pre[i]
        elif z * 2 > moves:
            if moves % 2 == 0:
                sm += (arr[i] + arr[i - 1]) * moves // 2
            else:
                sm += arr[i] * (moves // 2) + arr[i - 1] * ((moves // 2) + 1)
        ans = max(ans, sm)
    print(ans)
      
for _ in range(int(input())):
    solve()