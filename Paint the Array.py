def find_gcd(x, y):
    while(y):
        x, y = y, x % y 
    return x

def gcd_arr(a):
    if len(a) == 1:
        return a[0]
    gcd = find_gcd(a[0], a[1])
    for i in range(2, len(a)):
        gcd = find_gcd(gcd, a[i])
    return gcd
        
def check(x, a):
    for i in a:
        if i % x == 0:
            return False
    return True   
        
def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    aeven = []
    aodd = []
    
    for k in range(0, n, 2):
        aeven = aeven + [a[k]]
    for k in range(1, n, 2):
        aodd = aodd + [a[k]]
    
    x = gcd_arr(aeven)
    if check(x, aodd):
       print(x)
       return
   
    y = gcd_arr(aodd)
    if check(y, aeven):
       print(y)
       return
   
    print(0)

for _ in range(int(input())):
    solve()
    
    
    
    
    
    