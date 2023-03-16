import sys
input = lambda: sys.stdin.readline().rstrip("\n\r")
#file = open('inp.txt', 'r'); input = lambda: file.readline().rstrip("\n\r")

def neigh(i, j):
    return [[(i - 1, j), (i, j + 1)],
            [(i - 1, j), (i, j - 1)],
            [(i + 1, j), (i, j - 1)],
            [(i + 1, j), (i, j + 1)]]

def neighbour(i, j):
    return [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1),
            (i, j - 1), (i, j + 1),
            (i + 1, j - 1), (i + 1, j), (i + 1, j + 1)]

def solve():
    n, m = [int(i) for i in input().split()]
    a = []
    a.append(['.'] * (m + 2))
    for i in range(n):
        a.append(['.'] + [i for i in input()] + ['.'])
    a.append(['.'] * (m + 2))
    n += 2
    m += 2   
    num = 1

    for i in range(n):
        for j in range(m):
            if a[i][j] == '*':
                for k in neigh(i, j):
                    if a[k[0][0]][k[0][1]] == '*' and a[k[1][0]][k[1][1]] == '*':
                        a[i][j] = a[k[0][0]][k[0][1]] = a[k[1][0]][k[1][1]] = num
                        num += 1
    #for i in a: print(i)
    for i in range(n):
        for j in range(m):
            if a[i][j] == '*':
                print('No')
                return
            elif a[i][j] != '.':
                x = a[i][j]
                for k in neighbour(i, j):
                    if a[k[0]][k[1]] != x and a[k[0]][k[1]] != '.':
                        print('No')
                        return

    print('Yes')

for _ in range(int(input())):
    solve()
    