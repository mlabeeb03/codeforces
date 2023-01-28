import sys
input = lambda: sys.stdin.readline().rstrip("\n\r")
from collections import deque, Counter

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    a = Counter(a)
    dol = []
    for i in a:
        dol.append([i, a[i]])
    dol = deque(dol)
    ans = 0
    #print(dol)
    while dol:
        if dol[0][1] > 0:
            dol[0][1] -= 1
            eq = dol[0][0] + 1
            ind = 1
            while ind < len(dol) and dol[ind][0] == eq and dol[ind][1] > 0:
                dol[ind][1] -= 1
                eq += 1
                ind += 1
            ans += 1
        if dol[0][1] == 0:
            dol.popleft()
        #print(dol)
    print(ans)
        
 
for _ in range(int(input())):
    solve()