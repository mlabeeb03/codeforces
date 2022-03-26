# -*- coding: utf-8 -*-

n = int(input())
for i in range(n):
    x = input()
    turn = True
    while True:
        i = max(x.find('01'), x.find('10'))
        if i != -1:
            x = x[:i] + x[i+2:]
            turn = not turn
        else:
            if turn:
                print('NET')
            else:
                print('DA')
            break
    
