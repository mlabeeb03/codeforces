import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    pre = [0] + a[:]
    for i in range(1, n + 1):
        pre[i] += pre[i - 1]
    ans = n
    for i in range(1, n + 1):
        segs = [i]
        goal = pre[i]
        j = i
        k = i + 1
        while k <= n:
            if pre[k] - pre[j] < goal:
                k += 1
            elif pre[k] - pre[j] > goal:
                break
            else:
                segs.append(k - j)
                j = k
                k = j + 1
        if j == n and k == n + 1:
            ans = min(ans, max(segs))
    print(ans) 
                                   
for _ in range(int(input())):
    solve()
