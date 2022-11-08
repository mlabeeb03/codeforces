import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")

def solve():
    n = int(input())
    lid = list(map(int, input()))
    bok = list(map(int, input().split()))
    i = 0
    while i < n - 1:
        j = i + 1
        if lid[i] == 0 and lid[j] == 1:
            while j < n and bok[j] > bok[i] and lid[j] == 1:
                j += 1
            if j == n or lid[j] == 0:
                i += 1
            elif bok[j] <= bok[i] and lid[j] == 1:
                lid[i] = 1
                lid[j] = 0
            else:
                i += 1
        else:
            i += 1
    ans = 0
    for i in range(n):
        if lid[i] == 1:
            ans += bok[i]
    print(ans)
    
for _ in range(int(input())):
    solve()

    