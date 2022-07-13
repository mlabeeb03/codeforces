def solve():
    n = int(input())
    #u, v = map(int, input().split())    
    #u = list(map(int, input().split())) 
    #s = list(map(int, input().split())) 
    #a = list(map(str, input())) 
    
    graph = [[] for __ in range(n + 1)]
    ans = [-1] * (n - 1)
    for i in range(n - 1):
        x, y = map(int, input().split())
        graph[x] += [(y, i)]
        graph[y] += [(x, i)]
    if max(len(graph[i]) for i in range(n + 1)) > 2:
        print(-1)
        return
    cur, prev = 1, None
    while len(graph[cur]) != 1: 
        cur += 1
    for p in range(n - 1):
        for x, i in graph[cur]:
            if x != prev:
                ans[i] = [17, 2][p % 2]
                cur, prev = x, cur
                break
    print(*ans)
        
for _ in range(int(input())):
    solve()