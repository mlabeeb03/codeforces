import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")
from collections import Counter
def ln(n):
    x = 0
    while n > 0:
        n //= 10
        x += 1
    return x
def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ans = 0    
    arr = Counter(a)
    brr = Counter(b)
    for i in arr.keys():
        if i in brr:
            x = min(arr[i], brr[i])
            arr[i] -= x
            brr[i] -= x 
    
    c = []
    d = []
    for i in arr.keys():
        for j in range(arr[i]):
            c.append(i)
    for i in brr.keys():
        for j in range(brr[i]):
            d.append(i)
            
    for i in range(len(c)):
        if c[i] >= 10:
            c[i] = ln(c[i])
            ans += 1
        if d[i] >= 10:
            d[i] = ln(d[i])
            ans += 1
            
    arr = Counter(c)
    brr = Counter(d)
    for i in arr.keys():
        if i in brr:
            x = min(arr[i], brr[i])
            arr[i] -= x
            brr[i] -= x
    
    c = []
    d = []
    for i in arr.keys():
        for j in range(arr[i]):
            c.append(i)
    for i in brr.keys():
        for j in range(brr[i]):
            d.append(i)
    ans += len(c) * 2
    ans -= c.count(1)
    ans -= d.count(1)
    print(ans)
for _ in range(int(input())):
    solve()