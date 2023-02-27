import sys
input = lambda: sys.stdin.readline().rstrip("\n\r")
#file = open('inp.txt', 'r') ; input = lambda: file.readline().rstrip("\n\r")

def same(a, i, j):
    return (a[0] == i and a[1] == j) or (a[0] == j and a[1] == i)


def solve():
    n, m = map(int, input().split()) 
    g = [set() for i in range(n + 1)]
    edg = []
    for i in range(m):
        x, y = map(int, input().split()) 
        g[x].add(y)
        g[y].add(x)
        edg.append([x, y])
    
    if m == (n * (n - 1)) // 2:
        print(3)
        ind = 1
        done = 0
        for i in edg:
            if (i[0] == ind or i[1] == ind) and done == 0:
                print(1, end = ' ')
                done = 1
            elif (i[0] == ind or i[1] == ind):
                print(3, end = ' ')
            else:
                print(2, end = ' ')
        print()
        return

    ind = None
    mn = 1000000000000000
    for i in range(1, n + 1):
        if len(g[i]) < mn:
            mn = len(g[i])
            ind = i
    print(2)
    for i in edg:
        if i[0] == ind or i[1] == ind:
            print(1, end = ' ')
        else:
            print(2, end = ' ')
    print()
     
for _ in range(int(input())):
    solve()