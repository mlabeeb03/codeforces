import sys
input = sys.stdin.readline

def getXOR(a):
    x = a[0]
    for i in range(1, len(a)):
        x ^= a[i]
    return x
def solve():
    n = int(input())
    #n, x = map(int, input().split())    
    a = list(map(int, input().split()))
    
    inc = a[:]
    dec = a[:]
    
    for i in range(1, n):
        inc[i] ^= inc[i - 1]
    for i in range(n - 2, -1, -1):
        dec[i] ^= dec[i + 1]
        
    for i in range(n - 1):
        if inc[i] == dec[i + 1]:
            print('YES')
            return
        
    for i in range(n - 2):
        ixor = inc[i]
        for j in range(i + 1, n - 1):
            jxor = inc[j] ^ inc[i]
            kxor = dec[j + 1]
            if ixor == jxor and jxor == kxor:
                print('YES')
                return
    print('NO')
    return

for _ in range(int(input())):
    solve()

    