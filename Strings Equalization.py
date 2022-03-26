# -*- coding: utf-8 -*-

tcs = int(input())
for i in range(tcs):
    answer = False
    s = input()
    t = input()
    for j in range(len(s)):
        for k in range(len(t)):
            if s[j] == t[k]:
                answer = True
            
    if answer == True:
        print('YES')
    else:
        print('NO')
        

    