import sys
input = lambda: sys.stdin.readline().rstrip("\n\r")

def countz(x):
    ans = 0
    while x > 0:
        if x % 10 == 0:
            ans += 1
            x //= 10
        else:
            return ans

def solve():
    #n = int(input())
    n, m = map(int, input().split())
    #a = list(map(int, input().split()))
    
    
    initz = countz(n)
    while m > 0:
        did = 0
        for i in range(2, min(11, m + 1)):
            new = n * i
            newz = countz(new)
            if newz > initz:
                #print(n, i, m, n * i)
                initz = newz
                n = new
                m //= i
                did = 1
                break
        if did == 0:
            print(n * m)
            return
    print(n)


for _ in range(int(input())):
    solve()

    