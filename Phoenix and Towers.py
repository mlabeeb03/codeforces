from operator import itemgetter
def solve():
    #n = int(input())
    n, m, x = map(int, input().split())    
    a = list(map(int, input().split())) 
    #a = list(map(str, input())) 
    
    towers = [0] * m
    pairs = []
    for i in range(n):
        pairs.append([a[i], i])
    pairs.sort(key=itemgetter(0), reverse=True)

    i = 0
    while i < n:
        if towers[-1] >= towers[0]:
            for k in range(0, m):
                towers[k] += pairs[i][0]
                pairs[i][0] = k + 1
                i += 1
                if i == n:
                    break
        else:
            for k in range(m - 1, -1, -1):
                towers[k] += pairs[i][0]
                pairs[i][0] = k + 1
                i += 1
                if i == n:
                    break
    if abs(towers[0] - towers[-1]) > x:
        print('NO')
        return
    pairs.sort(key=itemgetter(1))
    print('YES')
    for i in range(n):
        print(pairs[i][0], end = ' ')
    print()
        
for _ in range(int(input())):
    solve()

    