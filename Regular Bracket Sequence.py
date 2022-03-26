# -*- coding: utf-8 -*-

def solve(s):
    if(s[0] == ')' or s[-1] == '(' or len(s) % 2 == 1):
        print('NO')
    else:
        print('YES')

tcs = int(input())
for i in range(tcs):
    s = input()
    solve(s)
    

    