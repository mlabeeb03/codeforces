import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    diff = 0
    for i in range(n):
        if a[i] != b[i]:
            diff += 1
    if diff == 0:
        print(0)
        return
    a1 = a.count(1)
    b1 = b.count(1)
    if a1 == b1 or diff == 1:
        print(1)
        return
    ans = min(diff, abs(a1 - b1) + 1)
    print(ans)
    
for _ in range(int(input())):
    solve()