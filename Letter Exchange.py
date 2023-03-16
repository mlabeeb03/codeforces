import sys
input = lambda: sys.stdin.readline().rstrip("\n\r")
#file = open('inp.txt', 'r'); input = lambda: file.readline().rstrip("\n\r")

dic = {'w': 0, 'i': 1, 'n': 2}
pic = {0: 'w', 1: 'i', 2: 'n'}

def solve():
    m = int(input())
    a = [list(map(str, input())) for i in range(m)]

    trade = [[[] for i in range(3)] for i in range(3)]

    for i in range(m):
        have = []
        dont = ['w', 'i', 'n']
        give = []
        for j in a[i]:
            if j not in have:
                have.append(j)
                dont.remove(j)
            else:
                give.append(j)
        for k in range(len(give)):
            trade[dic[give[k]]][dic[dont[k]]].append(i + 1)
    
    ans = []
    for i in range(3):
        for j in range(3):
            if i == j:
                continue
            while trade[i][j] and trade[j][i]:
                ans.append([trade[i][j].pop(), pic[i], trade[j][i].pop(), pic[j]])


    while trade[0][1]:
        t = trade[0][1][-1]
        ans.append([trade[0][1].pop(), 'w', trade[2][0].pop(), 'n'])
        trade[2][1].append(t)
        ans.append([trade[2][1].pop(), 'n', trade[1][2].pop(), 'i'])

    while trade[0][2]:
        t = trade[0][2][-1]
        ans.append([trade[0][2].pop(), 'w', trade[1][0].pop(), 'i'])
        trade[1][2].append(t)
        ans.append([trade[1][2].pop(), 'i', trade[2][1].pop(), 'n'])

    
    print(len(ans))
    for i in ans:
        print(*i)

for _ in range(int(input())):
    solve()
    