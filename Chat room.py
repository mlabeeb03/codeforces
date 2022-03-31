# -*- coding: utf-8 -*-

def solve(w):
    s = ['h','e','l','l','o']
    ind = 0
    for i in w:
        if i == s[ind]:
            ind += 1
            if ind == 5:
                print('YES')
                return
    print('NO')
    
w = input()
solve(w)


    