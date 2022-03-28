# -*- coding: utf-8 -*-

tcs = int(input())
for i in range(tcs):
    arr = input()
    first11 = arr.find('11')
    last00 = arr.rfind('00')
    
    if(first11 == -1 or last00 == -1):
        print('yes')
    elif (first11 < last00):
        print('no')
    else:
        print('yes')
        


    