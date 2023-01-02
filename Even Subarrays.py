import sys
input = lambda: sys.stdin.readline().rstrip("\n\r")


def solve(): 
    n = int(input())
    a = list(map(int, input().split()))
    
    ans = (n * (n + 1)) // 2
    
    occ = [0] * (2 * n)
    occ[0] = 1
    
    c = 0
    x = 0
    for i in range(n):
        x ^= a[i]
        for j in sq:
            if j ^ x < 2 * n:
                c += (occ[j ^ x])
        occ[x] += 1
    print(ans - c)
               
sq=[]
p=0
while p*p<=4*10**5:
    sq.append(p*p)
    p+=1
for _ in range(int(input())):
    solve()