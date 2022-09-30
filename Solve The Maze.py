import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")

def dfs(graph, start):
    visited = set() 
    stack = [start]
    while stack:
        start = stack[-1]
        if start not in visited:
            visited.add(start)
            for child in graph[start]:
                if child not in visited:
                    stack.append(child)
        else:
            stack.pop()
    return visited

def solve(): 
    n, m = list(map(int, input().split()))
    maze = [0]
    for i in range(n):
        maze += list(map(str, input()))
    #print('maze: ', maze)
    excluded = set()
    for i in range(1, n * m + 1):
        if maze[i] == '#':
            excluded.add(i)
        if maze[i] == 'B':
            if i // (m + 1) > 0 and maze[i - m] != 'B':
                excluded.add(i - m)
            if i % m != 1 and m > 1 and maze[i - 1] != 'B':
                excluded.add(i - 1)
            if i // m + (i % m != 0) != n and maze[i + m] != 'B':
                excluded.add(i + m)
            if i % m != 0 and maze[i + 1] != 'B':
                excluded.add(i + 1)
    
    g = [[] for i in range(n * m + 1)]
    g[0] = [0] * (n * m + 1)
    for i in range(1, n * m + 1):
        if i in excluded:
            continue
        if i // (m + 1) > 0 and i - m not in excluded:
            g[i].append(i - m)
            g[0][i] += 1
        if i % m != 1 and m > 1 and i - 1 not in excluded:
            g[i].append(i - 1)
            g[0][i] += 1
        if i // m + (i % m != 0) != n and i + m not in excluded:
            g[i].append(i + m)
            g[0][i] += 1
        if i % m != 0 and i + 1 not in excluded:
            g[i].append(i + 1)
            g[0][i] += 1
    
    good = []
    for i in range(1, n * m + 1):
        if maze[i] == 'G':
            good.append(i)
    visited = dfs(g, n * m)
    for i in good:
        if i not in visited:
            print('No')
            return
    print('Yes')

for _ in range(int(input())):
    solve()

    
    

    