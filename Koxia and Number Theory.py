for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    prime = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
    ans = 1
    if len(set(l)) != len(l):
        ans = 0
    for i in prime:
        l1 = [0]*i
        c = i
        for j in l:
            if l1[j%i] == 0:
                l1[j%i] = 1
            elif l1[j%i] == 1:
                l1[j%i] = 2
                c -= 1
        if c == 0:
            ans = 0
    if ans:
        print('YES')
    else:
        print('NO')