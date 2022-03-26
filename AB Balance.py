# -*- coding: utf-8 -*-

itr = int(input())
for i in range(itr):
    str = input()
    if str[0] != str[len(str)-1]:
        if str[0] == 'a':
            str = 'b' + str[1:]
        else:
            str = 'a' + str[1:]
    print(str)


    