import sys
input = lambda: sys.stdin.readline().rstrip("\n\r")

def check(val, a, n):
    cp = [0, 0]
    maxc1 = 0
    maxc2 = -1
    for i in range(n * 2 - 2):
        chk1 = []
        if cp[0] == 0 and cp[1] % 2 == 0:
            chk1 = [1, cp[1]]
        elif cp[0] == 1 and cp[1] % 2 == 0:
            chk1 = [1, cp[1] + 1]
        elif cp[0] == 1 and cp[1] % 2 == 1:
            chk1 = [0, cp[1]]
        elif cp[0] == 0 and cp[1] % 2 == 1:
            chk1 = [0, cp[1] + 1]
                    
        chk2 = []
        if cp[0] == 0:
            chk2 = [cp[0] + 1, cp[1] + 1]
        else:
            chk2 = [cp[0] - 1, cp[1] + 1]

        if a[chk1[0]][chk1[1]] <= val and a[chk2[0]][chk2[1]] <= val + 1:
            cp = chk1[:]
            val += 1
            if cp[0] == 0:
                maxc1 = max(maxc1, cp[1])
            else:
                maxc2 = max(maxc2, cp[1])                
        else:
            break 
    
    for i in range(cp[1] + 1, n):
        if a[cp[0]][i] > val:
            return 0
        else:
            cp = [cp[0], i]
            val += 1
    
    upto = -1    
    if cp[0] == 0:
        upto = maxc2
    else:
        upto = maxc1
    
    if a[cp[0] ^ 1][n - 1] > val:
        return 0
    else:
        cp = [cp[0] ^ 1, n - 1]
        val += 1
    
    for i in range(n - 2, upto, -1):
        if a[cp[0]][i] > val:
            return 0
        else:
            cp = [cp[0], i]
            val += 1
    return 1

def solve():
    n = int(input())
    a = [list(map(int, input().split())) for i in range(2)]
    
    l, r = 0, mx
    ans = mx
    while l <= r:
        m = (l + r) // 2
        if check(m, a, n):
            ans = m
            r = m - 1
        else:
            l = m + 1
    print(ans + n * 2 - 1)
    '''
    print(check(0, a, n))
    '''
    
mx = int(10E10)
for _ in range(int(input())):
    solve()

    