def sum1toN(n):
    return (n * (n + 1)) // 2

def solve():
    k, x = map(int, input().split())    
    #a = list(map(str, input())) 
    l = 1
    r = res = 2 * k - 1
    s = -1   
    while l <= r:
        m = (l + r) >> 1  
        if m < k:
            s = sum1toN(m)
        else:
            s = sum1toN(k) + sum1toN(k - 1) - sum1toN((2 * k - 1) - m)   
        if s >= x:
            res = m
            r = m - 1
        else:
            l = m + 1
    print(res)  
                       
    
for _ in range(int(input())):
    solve()

    