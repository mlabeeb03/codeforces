def solve():
    n = int(input())
    x = ((n - 1) // 4) + 1
    print('9' * (n - x), end = "")
    print('8' * x)
    

for __ in range(int(input())):
    solve()
                
    
    