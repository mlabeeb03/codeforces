def solve(clist):
    x = int(input())
    i = 1
    while(i*i*i <= x):
        if ((x - i*i*i) in clist):
            print('YES')
            return
        i += 1
    print('NO')
 
for _ in range(int(input())):
    clist = set({})
    i = 1
    while(i <= 10000):
        clist.add(i*i*i)
        i += 1
    solve(clist)



