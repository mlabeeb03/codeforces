import sys
input = lambda: sys.stdin.readline().rstrip("\n\r")

def solve(): 
    n, m = list(map(int, input().split()))

     
    c = [0] * (n + 1)
    for i in range(n, 0, -1):
        cnt = n // i
        c[i] = (cnt * (cnt - 1)) // 2
        j = 2 * i
        while j <= n:
            c[i] -= c[j]
            j += i
              
    price = 0
    for i in range(n, 1, -1):
        if c[i] < (i - 1):
            continue
        moves = c[i] // (i - 1)
        if moves * (i - 1) <= m:
            m -= moves * (i - 1)
            price += moves * i
        else:
            moves = m // (i - 1)
            m -= moves * (i - 1)
            price += moves * i
    if m == 0:
        print(price)
    else:
        print(-1)
        
for _ in range(int(input())):
    solve()