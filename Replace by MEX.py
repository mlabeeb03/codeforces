import sys
input = lambda: sys.stdin.readline().rstrip("\n\r")

def mex(a, n):
    s = set(a)
    for i in range(n + 1):
        if i not in s:
            return i
    
def solve():  
    n = int(input())
    a = list(map(int, input().split()))
    ans = []
    nind = n
    for i in range(2 * n):
        x = mex(a[:nind], nind)
        if x == nind:
            nind = max(1, nind - 1)
            a[nind] = x
            ans.append(nind + 1)
        else:
            a[min(x, nind - 1)] = x
            ans.append(min(x, nind - 1) + 1)
        
    #print(a)
    print(len(ans))
    print(*ans)
    #print()

for _ in range(int(input())):
    solve()


    