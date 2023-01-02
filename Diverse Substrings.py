import sys
input = lambda: sys.stdin.readline().rstrip("\n\r")

def solve():
    n = int(input())
    a = list(map(int, input()))
    ans = 0
    for i in range(n):
        cnt = [0] * 11
        unique = set()
        for j in range(i, min(n, i + 100)):            
            cnt[a[j]] += 1
            unique.add(a[j])
            if len(unique) >= max(cnt):
                ans += 1
    print(ans)

for _ in range(int(input())):
    solve()

    