import sys
input = lambda: sys.stdin.readline().rstrip("\n\r")


def solve():
    n = int(input())
    #n, m = list(map(int, input().split()))
    a = list(map(int, input().split()))
    if len(set(a)) == 1:
        print('NO')
        return
    
    a.sort(reverse = True)
    
    arr = a[:]
    arr[1] = a[-1]
    arr[-1] = a[1]
    print('YES')
    print(*arr)

for _ in range(int(input())):
    solve()