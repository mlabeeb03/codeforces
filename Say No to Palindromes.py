import sys
input = sys.stdin.readline
import math

def solve():
    #n = int(input())
    n, m = map(int, input().split())
    #a = list(map(int, input().split()))
    a = list(map(str, input()))
    combs = [['a','b','c'],['a','c','b'],['c','b','a'],['b','a','c'],['b','c','a'],['c','a','b']]
    anslist = [[0 for _ in range(n + 1)] for _ in range(6)]
    for i in range(6):
        if a[0] != combs[i][0]:
            anslist[i][1] = 1
        ind = 1
        for j in range(1, n):
            if a[j] != combs[i][ind]:
                anslist[i][j + 1] = anslist[i][j] + 1
            else:
                anslist[i][j + 1] = anslist[i][j]
            ind += 1
            if ind == 3:
                ind = 0
    
    for i in range(m):
        ans = math.inf
        l, r = map(int, input().split())
        for i in range(6):
            ans = min(ans, anslist[i][r] - anslist[i][l - 1])
        print(ans)
       
for _ in range(1):
    solve()

    