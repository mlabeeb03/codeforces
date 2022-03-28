# -*- coding: utf-8 -*-

import math
 
def isPrime(n):     
    if(n <= 1):
        return False
    if(n <= 3):
        return True     
    if(n % 2 == 0 or n % 3 == 0):
        return False     
    for i in range(5,int(math.sqrt(n) + 1), 6):
        if(n % i == 0 or n % (i + 2) == 0):
            return False    
    return True

def nextPrime(N):
    if (N <= 1):
        return 2 
    prime = N
    found = False 
    while(not found):
        prime = prime + 1
        if(isPrime(prime) == True):
            found = True 
    return prime

tcs = int(input())
for i in range(tcs):
    d = int(input())
    if d == 1:
        print('6')
    elif d == 2:
        print('15')
    else:
        j = nextPrime(d)
        k = nextPrime(j+d-1)
        print(j*k)