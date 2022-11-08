import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")
 
def solve():
    n, c = map(str, input().split())
    a = list(map(str, input()))
    if c == 'g':
        print(0)
        return
    n = int(n)   
    a = a[:] + a[:]
    n = 2 * n
    i = a.index(c)
    j = i + 1
    ans = 0
    while i < n and j < n:
        while j < n and a[j] != 'g':
            j += 1
        if j < n:
            ans = max(ans, j - i)
        i = j + 1
        while i < n and a[i] != c:
            i += 1
        j = i + 1
    print(ans)
                                   
for _ in range(int(input())):
    solve()