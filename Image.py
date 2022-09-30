import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")

def solve():
    #n = int(input())  
    r1 = list(map(str, input()))
    r2 = list(map(str, input()))
    
    d = {}
    for i in r1:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    for i in r2:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    print(len(d) - 1)

for _ in range(int(input())):
    solve()

    
    

    