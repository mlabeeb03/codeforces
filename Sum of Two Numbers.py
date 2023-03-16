import sys
input = lambda: sys.stdin.readline().rstrip("\n\r")

def check(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

def solve():
    n = int(input())
    if n % 2 == 0:
        print(n // 2, n // 2)
    else:
        x , y = n // 2, n // 2 + 1
        xsum = check(x)
        ysum = check(y)
        if xsum < ysum:
            x, y = y, x
        diff = abs(xsum - ysum)

        if diff == 1:
            print(x, y)
            return 

        a = [int(i) for i in str(x)]
        b = [int(i) for i in str(y)]

        #print(a)
        #print(b)

        if len(a) < len(b):
            a = [0] + a

        for i in range(min(len(a), len(b))):
            while diff > 1 and a[i] > 1 and b[i] < 9:
                a[i] -= 1
                b[i] += 1
                diff -= 2

        a = ''.join(str(i) for i in a)
        b = ''.join(str(i) for i in b)

        print(int(a), int(b))

for _ in range(int(input())):
    solve()
    