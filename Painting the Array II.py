import sys
input = lambda: sys.stdin.readline().rstrip("\n\r")

def solve():
    n = int(input())
    a = [0] + list(map(int, input().split()))
    
    pos = [n + 1] * (n + 1)
    nxt = [None] * (n + 1)
    for i in range(n, -1, -1):
        nxt[i] = pos[a[i]]
        pos[a[i]] = i

    ans = 0
    black = [0]
    white = [0]
    for i in range(1, n + 1):
        if a[i] != a[black[-1]] and a[i] == a[white[-1]]:
            white.append(i)
        elif a[i] != a[white[-1]] and a[i] == a[black[-1]]:
            black.append(i)
        elif a[i] != a[white[-1]] and a[i] != a[black[-1]]:
            ans += 1
            if nxt[white[-1]] > nxt[black[-1]]:
                white.append(i)
            else:
                black.append(i)
        else:
            black.append(i)

    print(ans)

for _ in range(1):
    solve()

    