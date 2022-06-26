def solve():
    n = int(input())
    #n, m = map(int, input().split())
    a = list(map(int, input().split()))
    
    ans = [0]
    
    for i in range(1, n):
        if a[i] == a[i - 1]:
            ans.append(0)
            continue
        
        x = a[i] | a[i - 1]
        ans.append(a[i] ^ x)
        a[i] = x
        
    print(*ans)
        
for __ in range(int(input())):
    solve()

   