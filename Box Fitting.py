import math
def solve():
    #n = int(input())
    n, W = map(int, input().split())    
    a = list(map(int, input().split())) 
    
    done = ans = 0
    t = [0] * 21
    for i in a:
        x = int(math.log2(i))
        t[x] += 1
        
    while done < n:
        ans += 1
        space = W
        for i in range(20, -1, -1):
            x = v[i]
            if t[i] == 0 or v[i] > space:
                continue
            y = space // v[i]
            space -= v[i] * min(y, t[i])
            done += min(y, t[i]) 
            t[i] -= min(y, t[i])
    print(ans)
    
v = [2 ** i for i in range(21)]       
for _ in range(int(input())):
    solve()

    