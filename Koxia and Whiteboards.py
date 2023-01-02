import sys
input = lambda: sys.stdin.readline().rstrip("\n\r")

def solve(): 
    n, m = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    for i in range(m):
        mi = a.index(min(a))
        a[mi] = b[i]
    print(sum(a))
    
for _ in range(int(input())):
    solve()


    