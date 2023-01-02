import sys
input = lambda: sys.stdin.readline().rstrip("\n\r")

def solve():
    n = int(input())   
    a = list(map(int, input().split()))
    
    zc = n
    for i in range(n):
        if a[i] % 10 == 5:
            a[i] += a[i] % 10
        if a[i] % 10 != 0:
            zc -= 1
            while a[i] % 10 != 2:
                a[i] += a[i] % 10
    #print(zc)
    if zc == n:
        #print(*a)
        if len(set(a)) == 1:
            print('Yes')
        else:
            print('No')
        return
    if zc == 0:                
        a.sort()
        #print(*a)
        for i in range(n - 1):
            if (a[i + 1] - a[i]) % 20 > 0:
                print('No')
                return
        print('Yes')
        return
    print('No')

for _ in range(int(input())):
    solve()
    #print()

    