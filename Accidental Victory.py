def win(pos, a):
    power = a[pos]
    for i in range(len(a)):
        if i == pos:
            continue
        if power < a[i]:
            return False
        power += a[i]
    return True

def solve():
    n = int(input())
    #n, k = map(int, input().split())    
    a = list(map(int, input().split())) 
    #a = list(map(str, input())) 
    
    b = a[:]
    a.sort()
    
    l = 0
    r = n - 1
    fnk = a[-1]
    while l <= r:
        m = (l + r) // 2
        if (win(m, a)):
            r = m - 1
            fnk = a[m]
        else:
            l = m + 1

    anslist = []
    for i in range(n):
        if b[i] >= fnk:
            anslist.append(i + 1)
    print(len(anslist))
    print(*anslist)
        
for _ in range(int(input())):
    solve()