import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")
from collections import Counter

def solve():
    #n = int(input())
    n, l, r = map(int, input().split())
    a = list(map(int, input().split()))
    
    lef = a[:l]
    rig = a[l:]
    
    ld = Counter(lef)
    rd = Counter(rig)
    
    for i in ld.keys():
        if i in rd:
            x = min(ld[i], rd[i])
            ld[i] -= x
            rd[i] -= x
    
    chng = abs(l - r) // 2
    if chng == 0:
        print(sum(ld.values()))
        return    
    ans = 0    
    if l > r:
        for i in ld.keys():
            if ld[i] > 1:
                x = ld[i] // 2
                if x >= chng:
                    ld[i] -= chng * 2
                    ans += chng
                    chng = 0
                    break
                else:
                    ld[i] -= x * 2
                    ans += x
                    chng -= x
    else:
        for i in rd.keys():
            if rd[i] > 1:
                x = rd[i] // 2
                if x >= chng:
                    rd[i] -= chng * 2
                    ans += chng
                    chng = 0
                    break
                else:
                    rd[i] -= x * 2
                    ans += x
                    chng -= x
                    
    if chng == 0:
        print(ans + sum(ld.values()))
        return
    print(ans + chng + (sum(ld.values()) + sum(rd.values())) // 2)
    
    
for _ in range(int(input())):
    solve()