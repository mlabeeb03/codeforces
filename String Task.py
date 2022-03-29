# -*- coding: utf-8 -*-

s = list(map(str, input()))
vow = ['a','e','i','o','u','y','A','E','I','O','U','Y']
s = [i for i in s if i not in vow]
for i in range(len(s)):
    s[i] = s[i].lower()
s = '.'+'.'.join(s)

print(s)
    