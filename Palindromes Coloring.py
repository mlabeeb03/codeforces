def solve():
    #n = int(input())
    n, k = map(int, input().split())    
    #a = list(map(int, input().split())) 
    a = list(map(str, input())) 
    
    dic = {}
    for i in a:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1           
    v = list(dic.values())
    pairs = singles = 0
    for i in v:
        if i % 2 == 0:
            pairs += i // 2
            i = 0
        else:
            pairs += (i - 1) // 2
            singles += 1
    
    ans = 2 * (pairs // k)  
    pairs = max(0, pairs - (ans // 2) * k)
    singles += 2 * pairs     
    if singles >= k:
        ans += 1
    print(ans)
    
for _ in range(int(input())):
    solve()

    