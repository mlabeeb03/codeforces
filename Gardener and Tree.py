import sys
input = lambda: sys.stdin.readline().rstrip("\n\r")

def solve():
    ext = input()
    n, k = map(int, input().split())
    if n == 1:
        print(0)
        return
    graph = [[0, set()] for i in range(n + 1)]
    for i in range(n - 1):
        x, y = map(int, input().split())
        graph[x][0] += 1
        graph[y][0] += 1
        graph[x][1].add(y)
        graph[y][1].add(x)
    
    leaves = []
    for i in range(1, n + 1):
        if graph[i][0] == 1:
            leaves.append(i)
                
    ans = n
    for i in range(k): 
        if ans == 0:
            break
        new = []
        ans -= len(leaves)
        if len(leaves) == 1:
            break      
        for j in leaves:
            x = list(graph[j][1])[0]
            graph[x][1].remove(j)
            graph[x][0] -= 1
            if graph[x][0] == 1:
                new.append(x)
            elif graph[x][0] == 0:
                break
        leaves = new[:]
        
    print(ans)
    
for _ in range(int(input())):
    solve()

    