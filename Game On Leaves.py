import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")

def solve():
    n, x = map(int, input().split())
    arr = []
    for i in range(n + 1):
        arr.append(set())
    for i in range(n - 1):
        a, b = map(int, input().split())
        arr[a].add(b)
        arr[b].add(a)
    t = 0
    #print(len(arr[x]))
    while True:
        if len(arr[x]) < 2:
            return t
        elif len(arr[x]) == 2:
            picked = 0
            for i in range(1, n + 1):
                if i == x:
                    continue
                if len(arr[i]) == 1:
                    q = arr[i].pop()
                    if q == x:
                        arr[i].add(q)
                    else:
                        arr[q].remove(i)
                        t = 1 - t
                        picked = 1
                        break
            if picked == 0:
                return 1 - t
        else:
            for i in range(1, n + 1):
                if i == x:
                    continue
                if len(arr[i]) == 1:
                    q = arr[i].pop()
                    arr[q].remove(i)
                    t = 1 - t
                    break
                                   
for _ in range(int(input())):
    x = solve()
    if x == 0:
        print('Ayush')
    else:
        print('Ashish')