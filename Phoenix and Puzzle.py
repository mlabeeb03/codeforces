# -*- coding: utf-8 -*-

import math

def isSquare(num):
    sr = int(math.sqrt(num))
    return (sr * sr == num)
def solve(s):
    if(((s%2 == 0 and isSquare(s/2))  or math.sqrt(s) % 2 == 0) and s != 1):
        print('YES')
    else:
        print('NO')       

tcs = int(input())
for i in range(tcs):
    s = int(input())
    solve(s)
    

    