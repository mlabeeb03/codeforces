def solve():
    #n = int(input())
    a, b, k = map(int, input().split())    
    b = list(map(int, input().split())) 
    g = list(map(int, input().split())) 
    #a = list(map(str, input())) 
    
    bot = {}
    gin = {}
    for i in b:
        if i in bot:
            bot[i] += 1
        else:
            bot[i] = 1
    for i in g:
        if i in gin:
            gin[i] += 1
        else:
            gin[i] = 1
    
    ans = 0
    for i in range(k):
        ans += (k - 1) - (bot[b[i]] - 1) - (gin[g[i]] - 1)
  
    print(ans // 2)
        
for _ in range(int(input())):
    solve()

    