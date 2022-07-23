import math
 
def check_prime(x):
    n = 2
    while n <= int(math.sqrt(x)):
        if x%n == 0: return False
        n += 1
    
    return True
 
t = int(input())
 
for _ in range(t):
    n = int(input())
    
    if n == 1: print('FastestFinger')
 
    elif n%2 == 1 or n == 2: print('Ashishgup')
 
    else:
        x = 1
        while n%2 == 0:
            x *= 2
            n >>= 1
            
        if n == 1:
            print('FastestFinger')
        else:
            if (x == 2):
                if (check_prime(n)):
                    print('FastestFinger')
                else:
                    print('Ashishgup')
            else:
                print('Ashishgup')