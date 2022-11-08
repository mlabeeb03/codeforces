import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")

def solve():
    n = int(input())
    a = list(map(int, input()))
    tot = 0
    ew0 = ew1 = 0
    lstew0 = []
    lstew1 = []
    lstans = []
    for i in range(n):
        if a[i] == 0:
            if ew1 == 0:
                tot += 1
                ew0 += 1
                lstew0.append(tot)
            else:
                ew1 -= 1
                ew0 += 1
                lstew0.append(lstew1.pop())
            lstans.append(lstew0[-1])
        else:
            if ew0 == 0:
                tot += 1
                ew1 += 1
                lstew1.append(tot)
            else:
                ew0 -= 1
                ew1 += 1
                lstew1.append(lstew0.pop())
            lstans.append(lstew1[-1])
    print(tot)
    print(*lstans)
        
for _ in range(int(input())):
    solve()

    