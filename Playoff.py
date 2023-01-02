import sys
input = lambda: sys.stdin.readline().rstrip("\n\r")

def solve():
    n = int(input())   
    a = list(map(int, input()))
    #print(a)
    
    l = 0
    lp = 0
    r = 2 ** n
    rp = 0
    
    for i in a:
        if i == 1:
            l += 2 ** lp
            lp += 1
        else:
            r -= 2 ** rp
            rp += 1
    
    #print(l, r)
    ans = [i for i in range(l + 1, r + 1)]
    print(*ans)
            

for _ in range(1):
    solve()

    