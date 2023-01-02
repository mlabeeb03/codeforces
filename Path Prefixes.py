import sys
input = lambda: sys.stdin.readline().rstrip("\n\r")
import bisect

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
def dfs(visited, graph, node, arr, brr, ans):
    if node not in visited:
        visited.add(node)
        for neighbour in graph[node]:
            arr.append(arr[-1] + neighbour[1])
            brr.append(brr[-1] + neighbour[2])
            ans[neighbour[0]] = bisect.bisect_right(brr, arr[-1]) - 1
            yield dfs(visited, graph, neighbour[0], arr, brr, ans)
    arr.pop()
    brr.pop()
    yield

def solve():
    n = int(input())   
    g = [[] for i in range(n + 1)]
    for i in range(n - 1):
        p, a, b = map(int, input().split())
        g[p].append([i + 2, a, b])
        
    visited = set()
    arr = [0]
    brr = [0]
    ans = [None] * (n + 1)
    dfs(visited, g, 1, arr, brr, ans)
    print(*ans[2:])

for _ in range(int(input())):
    solve()

    