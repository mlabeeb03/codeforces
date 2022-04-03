tcs = int(input())
for i in range(tcs):
    a = input()
    b = input()
    al = len(a)
    bl = len(b)
    tab = [[0 for _ in range(bl+1)] for _ in range(al+1)]
    
    for j in range(al):
        for k in range(bl):
            if a[j] == b[k]:
                tab[j+1][k+1] = 1 + tab[j][k]
    x = max(map(max, tab))
    print((al - x) + (bl - x))
    