import sys
input = lambda: sys.stdin.readline().rstrip("\n\r")

def check(t1, n):
    ans1 = 0
    numz = 0
    for i in range(n - 1, -1, -1):
        if t1[i] == 0:
            numz += 1
        else:
            ans1 += numz
    return ans1
            
def solve():
    n = int(input())   
    a = list(map(int, input().split()))
    
    t1 = a[:]
    for i in range(n):
        if t1[i] == 0:
            t1[i] = 1
            break    
    
    t2 = a[:]
    for i in range(n - 1, -1, -1):
        if t2[i] == 1:
            t2[i] = 0
            break

    print(max(check(t1, n), check(t2, n), check(a, n)))
    
    

for _ in range(int(input())):
    solve()

    