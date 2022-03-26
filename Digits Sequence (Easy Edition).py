# -*- coding: utf-8 -*-

line = [];
for i in range(10000+1):
    line.extend(list(str(i)))
n = int(input())
print(line[n])

    