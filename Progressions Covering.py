import sys
input = lambda: sys.stdin.readline().rstrip("\n\r")
                
def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    allowed = []
    for i in range(n):
        if i + 1 <= k:
            allowed.append(i + 1)
        else:
            allowed.append(k)
    
    moves, totsum, totmin = 0, 0, 0
    minmin = [0] * n
    for i in range(n - 1, -1, -1):
        totsum -= totmin
        totmin -= minmin[i]       
        a[i] -= totsum
        #print('a', totsum, totmin, a[i])
        if a[i] <= 0:
            continue
        this = (a[i] // allowed[i]) + (a[i] % allowed[i] > 0)
        moves += this
        totsum += allowed[i] * this
        totmin += this
        minmin[i - allowed[i]] += this
        #print('b', totsum, totmin, a[i])
    #print(minmin)
    print(moves)
        
for _ in range(1):
    solve()

    