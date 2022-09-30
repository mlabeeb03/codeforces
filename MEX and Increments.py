import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")
import collections

def solve():
    n = int(input())  
    a = list(map(int, input().split()))
    d = collections.Counter(a)
    fd = dict(d)
    
    price = [-1] * (n + 1)
    ks = []
    vs = []
    
    if 0 in d:
        price[0] = 0
        d[0] -= 1
        if d[0] > 0:
            ks.append(0)
            vs.append(d[0])
    else:
        price[0] = -1
        
    for i in range(1, n + 1):
        if price[i - 1] == -1:
            price[i] = -1
            continue
        if i in d:
            price[i] = price[i - 1]
            d[i] -= 1
            if d[i] > 0:
                ks.append(i)
                vs.append(d[i])
        else:
            if len(ks) > 0:
                price[i] = price[i - 1] + (i - ks[-1])
                vs[-1] -= 1
                if vs[-1] == 0:
                    ks.pop()
                    vs.pop()
            else:
                break
    #print(price)
    if 0 in fd:
        print(fd[0], end = ' ')
    else:
        print(0, end = ' ')
    for i in range(1, n + 1):
        if price[i - 1] == -1:
            print(-1, end = ' ')
            continue
        if i in fd:
            print(price[i - 1] + fd[i], end = ' ')
        else:
            print(price[i - 1], end = ' ')
    print()
    #print()

for _ in range(int(input())):
    solve()

    
    

    