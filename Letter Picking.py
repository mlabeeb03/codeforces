import sys
input = lambda: sys.stdin.readline().rstrip("\n\r")

def solve():
    a = list(map(str, input()))
    l, r = 0, len(a) - 1
    while l < r and a[l] == a[r]:
        l += 1
        r -= 1
    while l < r and a[l] == a[l + 1]:
        l += 2
    if l > r:
        print('Draw')
    else:
        print('Alice')
    
for _ in range(int(input())):
    solve()

    