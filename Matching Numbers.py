import sys
input = lambda: sys.stdin.readline().rstrip("\n\r")

def solve():
    n = int(input())
    if n % 2 == 0:
        print('No')
        return
    arr = list(range(1, 2 * n + 1))
    #print(arr)
    i = n - 1
    j = n
    ans = []
    for x in range(n // 2 + 1):
        ans.append([arr[i], arr[j]])
        i -= 1
        j += 2
    j = n + 1
    for x in range(n // 2):
        ans.append([arr[i], arr[j]])
        i -= 1
        j += 2
    print('Yes')
    for x in ans:
        print(*x)

for _ in range(int(input())):
    solve()
    