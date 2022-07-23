import sys
input = sys.stdin.readline

def solve():
    n, k = map(int, input().split())    
    a = list(map(int, input().split()))
    arr = []
    count = [n] * 31
    for i in a:
        x = format(i, '031b')
        arr.append(list(map(int, x)))
        for j in range(31):
            if x[j] == '1':
                count[j] -= 1
    ans = 0
    for i in range(31):
        if count[i] <= k:
            k -= count[i]
            ans += 2 ** (30 - i)
    print(ans)

for _ in range(int(input())):
    solve()

    