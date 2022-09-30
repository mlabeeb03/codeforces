def solve():
    n = int(input())
    val = 0
    tot = 0
    for i in range(2, 41):
        if i**10 >= n:
            val = i
            tot = i**10
            break
    lsm = tot
    rsm = 1
    l = 10
    r = 0
    for i in range(10):
        if (lsm//val) * (val - 1) * rsm >= n:
            lsm//=val
            rsm*=val-1
            l-=1
            r+=1
        else:
            break
    lst = ['c','o','d','e','f','o','r','c','e','s']
    for i in range(l):
        print(lst[i]*val, end='')
    for i in range(l, 10):
        print(lst[i]*(val-1), end='')
    print()

for _ in range(1):
    solve()

    