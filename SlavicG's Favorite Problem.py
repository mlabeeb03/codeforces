import sys
input = lambda: sys.stdin.readline().rstrip("\n\r")

from types import GeneratorType
def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc

@bootstrap
def dfs(visited, graph, node, ans, arr):
    if node not in visited:
        visited.add(node)
        for neighbour in graph[node]:
            if neighbour[0] not in visited:
                arr.append(arr[-1] ^ neighbour[1])
                ans[neighbour[0]] = arr[-1]
                yield dfs(visited, graph, neighbour[0], ans, arr)
                arr.pop()
    yield

    
def solve():
    n, a, b = map(int, input().split())
    g = [[] for i in range(n + 1)]
    for i in range(n - 1):
        u, v, w = map(int, input().split())
        g[u].append([v, w])
        g[v].append([u, w])
        
    visited = set()
    ans = [None] * (n + 1)
    arr = [0]
    dfs(visited, g, b, ans, arr)
    ola = set(ans[1:])
    #print(*ans[1:])
    ola.remove(None)
    
    visited = set({b})
    ans = [None] * (n + 1)
    arr = [0]
    dfs(visited, g, a, ans, arr)
    bola = set(ans[1:])
    #print(*ans[1:])
    bola.remove(None)
    
    if 0 in ola:
        print('Yes')
        return
    for i in ola:
        if i in bola:
            print('Yes')
            return
    print('No')
    
for _ in range(int(input())):
    '''
    if _ == 52:
        s = ""
        n, a, b = map(int, input().split())
        s += str(n) + "," + str(a) + "," + str(b) + ","
        for i in range(n - 1):
            u, v, w = map(int, input().split())
            s += str(u) + "," + str(v) + "," + str(w) + ","
        print(s)
        continue
    '''
    solve()

    