def solve():
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    ans = 0
    for i in range(k):
        x = 0
        for j in range(n - 1):
            if h[j] < h[j+1]:
                ans = j + 1
                h[j] += 1
                x = 1
                break
        if x == 0:
            print(-1)
            return
    print(ans) 

for _ in range(int(input())):
    solve()

    