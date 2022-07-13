def solve():
    #n = int(input())
    n, k = map(int, input().split())    
    a = list(map(int, input().split())) 
    #a = list(map(str, input())) 
    
    mx = []
    for i in range(n - 1):
        x = a[i + 1] - a[i]
        mx.append(int('9' * x))
    mx.append(int(10E9))
    
    ans = 0
    k += 1
    i = 0
    while k > 0:
        if k >= mx[i]:
            ans += mx[i] * 10**a[i]
            k -= mx[i]
            i += 1
        else:
            ans += k * 10**a[i]
            break
    print(ans)   
        
for _ in range(int(input())):
    solve()