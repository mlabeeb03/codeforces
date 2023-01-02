import sys
input = lambda: sys.stdin.readline().rstrip("\n\r")

def solve(): 
    n, m = list(map(int, input().split()))
    l, r = 1, n
    while l < r:
        print(r, l, end = ' ')
        l += 1
        r -= 1
    if n % 2 == 1:
        print(l)
    else:
        print()
        
for _ in range(int(input())):
    solve()


    