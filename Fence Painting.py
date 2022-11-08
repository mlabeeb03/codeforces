import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")

def solve():
    n, m = map(int, input().split())    
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    
    if c[-1] not in b:
        print('NO')
        return
    ext = None
    for i in range(n - 1, -1, -1):
        if b[i] == c[-1] and a[i] != b[i]:
            ext = i + 1
    if ext is None:
        ext = b.index(c[-1]) + 1    
    dic = {}
    for i in range(n):
        if a[i] != b[i]:
            if b[i] in dic:
                dic[b[i]].append(i + 1)
            else:
                dic[b[i]] = [0, i + 1]
    ans = []
    for i in range(m):
        if c[i] not in dic or dic[c[i]][-1] == 0:
            ans.append(ext)
        else:
            ans.append(dic[c[i]].pop())
    for i in dic.keys():
        if dic[i][-1] != 0:
            print('NO')
            return
    print('YES')
    print(*ans)
    
for _ in range(int(input())):
    solve()

    