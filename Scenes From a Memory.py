# -*- coding: utf-8 -*-
  
def checkPairs(numDig, dig):
    for i in range(numDig - 1):
        for j in range(i + 1, numDig):
            if(dig[i] == dig[j]):
                print(2)
                print(dig[i]*2)
                return True
    return False
def solve(numDig, dig):
    for i in range(numDig):
        if dig[i] in ['1','4','6','8','9']:
            print(1)
            print(dig[i])
            return
    if (numDig == 2):
        print(2)
        print(''.join(dig))
    elif checkPairs(numDig, dig):
        return
    else:
        print(2)
        while(len(dig) != 2):
            try:
                dig.remove('3')
            except:
                dig.remove('7')
        print(''.join(dig))
      
tcs = int(input())
for i in range(tcs):
    numDig = int(input())
    dig = list(map(str, input()))
    solve(numDig, dig)
    
   
        
  
        
    
            
    
    