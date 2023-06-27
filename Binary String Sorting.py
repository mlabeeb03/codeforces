import sys
try:
    file = open('inp.txt', 'r')
    input = lambda: file.readline().rstrip("\n\r")
except:
    input = lambda: sys.stdin.readline().rstrip("\n\r")
def ini():
    return(int(input()))
def inl():
    return(list(map(str,input().split())))
def inli():
    return(list(map(int,input().split())))
def ins():
    return([i for i in input()])
def insi():
    return([int(i) for i in input()])
def inv():
    return(map(int,input().split()))

def solve():
    a = insi()
    n = len(a)
    if n == 1:
        print(0)
        return 
    curr1 = 0
    curr0 = [int(a[-1] == 0)] * n
    for i in range(n - 2, -1, -1):
        curr0[i] = int(a[i] == 0) + curr0[i + 1]
    curr0.append(0)
    # print(a)
    # print(curr0)
    costs, costd, ans = int(1E12), int(1E12) + 1, float("inf")
    for i in range(n):
        ans = min(ans, (curr1 + curr0[i+1]) * costd)
        try:
            if a[i] == 1 and a[i + 1] == 0:
                ans = min(ans, costs + ((curr1+curr0[i+2])*costd))
        except:
            pass
        curr1 += int(a[i] == 1)
        # print(ans)
    print(ans)
     
for _ in range(int(input())):
    solve()
