import sys
input = lambda: sys.stdin.readline().rstrip("\r\t")

def solve():
    l = int(input())
    a = list(map(int, input().split()))
    p = a.count(1)
    n = a.count(-1)
    if (p + n) % 2 > 0:
        print(-1)
        return
    if p == n:
        print(l)
        for i in range(l):
            print(i + 1, i + 1)
        return
    num = 0
    count = abs(p - n) // 2
    if p > n:
        num = 1
    else:
        num = -1
    ans = []
    ind = l - 1
    k = 0
    while ind > -1:
        if a[ind] == num and count > 0 and ind > 0:
            ans.append([ind, ind + 1])
            count -= 1
            ind -= 2
        else:
            ans.append([ind + 1, ind + 1])
            ind -= 1
        k += 1
    if count > 0:
        print(-1)
        return
    print(k)
    for i in range(len(ans) - 1, -1, -1):
        print(*ans[i])
        
for _ in range(int(input())):
    solve()
    
    

    