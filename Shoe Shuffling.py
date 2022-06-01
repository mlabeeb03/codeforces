def solve():
    n = int(input())
    a = list(map(int, input().split()))
    newn = []
    dic = {}
    for i in a:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
            
    for v in dic.values():
        if v == 1:
            print(-1)
            return
        
    for v in dic.values():
        x = len(newn)
        for i in range(1, v+1):
            newn.append(((i % v) + 1) + x)
            
    print(*newn)
for __ in range(int(input())):   
    solve()
                
    
    