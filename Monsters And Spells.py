import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")
 
def solve():
    n = int(input())
    k = [0]
    for i in list(map(int, input().split())):   
        k.append(i) 
    h = [0]
    for i in list(map(int, input().split())):   
        h.append(i)
    i = n
    ans = 0
    while i > 0:
        poneat = k[i] - h[i] + 1
        j = i - 1
        while j > 0 and poneat <= k[j]:
            poneat = min(poneat, k[j] - h[j] + 1)
            j -= 1
        t = k[i] - poneat + 1
        ans += (t * (t + 1)) // 2
        i = j
    print(ans)              

for _ in range(int(input())):   
    solve()