# -*- coding: utf-8 -*-

tcs = int(input())
for i in range(tcs):
    threshold = 0
    ind = []
    length = int(input())
    s = input()
    t = input() 
    for j in range(length):
        if s[j] != t[j]:
            threshold += 1
            ind.append(j)
            
    if threshold != 2:
        print('NO')
    else:
        if s[ind[0]] == s[ind[1]] and t[ind[0]] == t[ind[1]]:
            print('YES')
        else:
            print('NO')
        

    