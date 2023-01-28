import sys
input = lambda: sys.stdin.readline().rstrip("\n\r")

def act(g, start, par):
    vis = set([par])
    stack = [start]
    while stack:
        x = stack[-1]
        if x not in vis:
            vis.add(x)
            if col[x] != col[start]:
                return False
            for c in g[x]:
                if c not in vis:
                    stack.append(c)
        else:
            stack.pop()
    return True
                
    
def dfs(g, s):
    for i in g[s]:
        #print(s, i)
        if act(g, i, s) == False:
            return False
    return True

n = int(input())
g = [[] for i in range(n + 1)]
e = []
for i in range(n - 1):
    x, y = list(map(int, input().split()))
    g[x].append(y)
    g[y].append(x)
    e.append([x, y])
col = [None] + list(map(int, input().split()))

if len(set(col[1:])) == 1:
    print('YES')
    print(1)
else:
    for i in e:
        if col[i[0]] != col[i[1]]:
            if dfs(g, i[0]):
                print('YES')
                print(i[0])
            elif dfs(g, i[1]):
                print('YES')
                print(i[1])
            else:
                print('NO')
            break

#print(g)
#print(e)





