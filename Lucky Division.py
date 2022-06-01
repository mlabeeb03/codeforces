def solve():
    n = int(input())
    
    arr = [4,7,47,74,447,477,774,744]
    
    for i in arr:
        if n % i == 0:
            print('YES')
            return
    print('NO')
    
solve()
                
    
    