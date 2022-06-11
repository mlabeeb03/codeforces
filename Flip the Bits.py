def solve():
    n = int(input())
    a = list(map(int, input()))
    b = list(map(int, input()))
    
    if n % 2 == 1 and a[-1] != b[-1]:
        print('NO')
        return
    
    pre = [0] * n
    indices = [0]
    zc = 0
    oc = 0
    for i in range(n):
        if a[i] == 0:
            zc += 1
        else:
            oc += 1
        if zc == oc:
            pre[i] = 1
            indices.append(i + 1)
            
    #print(a)
    #print(b)
    #print(pre)
    #print(indices)
    
    k = len(indices)
    w = 0
    for i in range(k - 1):
        w = 1
        x = y = 0
        for j in range(indices[i], indices[i + 1]):
            if a[j] == b[j]:
                x = 1
            if a[j] != b[j]:
                y = 1
        if x != 0 and y != 0:
            print('NO')
            return
    x = 0
    for j in range(indices[k - 1], n):
        if a[j] != b[j]:
            x = 1
    if x == 1:
        print('NO')
        return
            
    if w == 1 or a == b:
        print('YES')
    else:
        print('NO')

for _ in range(int(input())):
    solve()
    
