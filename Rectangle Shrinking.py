import sys
import heapq as hq
input = lambda: sys.stdin.readline().rstrip("\n\r")
#file = open('inp.txt', 'r'); input = lambda: file.readline().rstrip("\n\r")

def solve():
    n = int(input())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())) + [i])
    a.sort(key = lambda x: x[1])
    for i in range(n):
        a[i] += [i]

    p1 = p2 = i = 0
    q = []

    while i < n:
        '''
        print('p1 p2:', p1, p2)
        print('a[i]:', a[i])
        print('queue:', q)
        print('..........')
        for x in a:
            print(x)
        print()
        '''
        if a[i][0] == 1 and a[i][2] == 1:
            if a[i][3] <= p1:
                for j in range(4): a[i][j] = 0
            else:
                a[i][1] = max(p1 + 1, a[i][1])
                p1 = a[i][3]
                hq.heappush(q, [-a[i][3], a[i][-2], a[i][-1]])
            i += 1
        elif a[i][0] == 2 and a[i][2] == 2:
            if a[i][3] <= p2:
                for j in range(4): a[i][j] = 0
            else:
                a[i][1] = max(p2 + 1, a[i][1])
                p2 = a[i][3]
                hq.heappush(q, [-a[i][3], a[i][-2], a[i][-1]])
            i += 1
        elif a[i][0] == 1 and a[i][2] == 2:
            if p1 >= a[i][3]:
                a[i][0] = 2
                continue
            if p2 >= a[i][3]:
                a[i][2] = 1
                continue
            else:
                p1 = p2 = a[i][3]
                while q:
                    x = hq.heappop(q)
                    #print('x:', x, a[x[2]])

                    if a[x[2]][1] >= a[i][1]:
                        for j in range(4): a[x[2]][j] = 0
                    elif a[x[2]][1] < a[i][1] and a[x[2]][3] >= a[i][1]:
                        a[x[2]][3] = a[i][1] - 1
                    else:
                        hq.heappush(q, x)
                        break
                hq.heappush(q, [-a[i][3], a[i][-2], a[i][-1]])
                i += 1

    '''
    print('p1 p2:', p1, p2)
    print('queue:', q)
    print('..........')
    for x in a:
        print(x)
    print()
    '''

    ans = 0
    a.sort(key = lambda x: x[4])
    for i in a:
        if i[0] != 0:
            ans += ((i[2] - i[0]) + 1) * ((i[3] - i[1]) + 1)
    print(ans)
    for i in a:
        print(*i[:-2])

for _ in range(int(input())):
    solve()
    