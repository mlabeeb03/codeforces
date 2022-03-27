# -*- coding: utf-8 -*-

def numOfBlocks(s, n):
    if n == 1:
        return 1
    else:
        b = 1
        for i in range(len(s) - 1):
            if s[i] != s[i+1]:
                b += 1
        return b
      
tcs = int(input())
for i in range(tcs):
    n, a, b = [int(x) for x in input().split()]
    s = input()
    
    m = numOfBlocks(s, n)
    #print(m)
    if b > 0:
        print(a*n+b*n)
    else:    
        print(a*n+(int(m/2)+1)*b)
    
   
        
  
        
    
            
    
    