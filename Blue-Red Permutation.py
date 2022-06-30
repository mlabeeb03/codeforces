def solve():
    n = int(input())
    a = list(map(int, input().split()))   
    c = input()
    
    red = []
    blue = []
    rlen = blen = 0
    for i in range(n):
        if c[i] == 'B':
            blue.append(a[i])
            blen += 1
        else:
            red.append(a[i])
            rlen += 1
    blue.sort()
    red.sort()
    
    for i in range(blen):
        if blue[i] < i + 1:
            print('NO')
            return
    for i in range(rlen):
        if red[i] > i + blen + 1:
            print('NO')
            return
    
    print('YES')
           
for _ in range(int(input())):
    solve()