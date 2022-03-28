# -*- coding: utf-8 -*-

tcs = int(input())
for i in range(tcs):
    n = int(input())
    br = list(map(str, input()))
    answer = 0
    opened = 0
    for i in range(n):
        if(br[i] == ')' and opened == 0):
            answer += 1
        elif(br[i] == '('):
            opened += 1
        else:
            opened -= 1
    print(answer)

        


    