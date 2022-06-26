def solve():
    n = int(input())
    #n, m = map(int, input().split())
    a = list(map(int, input().split()))
    #a = list(map(int, input()))  
   
    arr = [a[0]]
    for i in range(1, n):
        if a[i] == arr[-1]:
            continue
        arr.append(a[i])
        
    ans = 1000000000
    dic = {}
    for i in arr:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 2
    dic[arr[0]] -= 1
    dic[arr[-1]] -= 1
            
    for i in dic.values():
        ans = min(ans, i)
            
    print(ans)
    
for __ in range(int(input())):
    solve()

   