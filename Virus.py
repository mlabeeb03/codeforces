import sys
input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    inf = list(map(int, input().split()))
    
    inf.sort()
    l = len(inf)
    if l == 1:
        print(2)
        return
    if l == n:
        print(n)
        return
    chunks = []
    for i in range(l - 1):
        chunks.append(max(0, (inf[i + 1] - inf[i]) - 1))
    chunks.append((inf[0] - 1) + (n - inf[-1]))
    chunks.sort(reverse = True)
    saved = 0
    if chunks[0] == 1:
        saved = 1
        print(n - 1)
        return
    else:
        saved = chunks[0] - 1
    dif = 4
    for i in range(1, l):
        if chunks[i] - dif == 1:
            saved += 1
            print(n - saved)
            return
        saved += max(0, (chunks[i] - dif) - 1)
        dif += 4
    print(n - saved)
            
for _ in range(int(input())):
    solve()

    