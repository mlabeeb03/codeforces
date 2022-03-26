# -*- coding: utf-8 -*-

from collections import deque

def solve(s):
    if s == 1:
        print(1)
    elif s == 2:
        print(-1)
    else:
        arr = [[None for _ in range(s)] for _ in range(s)]
        num1 = 1
        num2 = 0
        for i in range(s):
            for j in range(s):
                arr[i][j] = num1 + num2 * s
                num2 += 1
            num1 += 1
            num2 = 0        
        for i in range(s):
            item = deque(arr[i])
            item.rotate(i%s+1)
            arr[i] = item
        for i in range(s):
            print(*arr[i])
    
       

tcs = int(input())
for i in range(tcs):
    s = int(input())
    solve(s)
    

    