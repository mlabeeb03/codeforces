# -*- coding: utf-8 -*-

for i in range(int(input())):
    n, m, x, y = map(int, input().split())
    sqr = []
        
    for row in range(n):
        sqr.append(list(map(str, input())))
            
    if x*2 <= y:
        print(x * (sum(k.count('.') for k in sqr)))
    else:
        price = 0
        for row in sqr:
            i = 0
            while(True):
                ocr = 0
                while(row[i] == '.'):
                    ocr += 1
                    i += 1
                    if i > m-1:
                        break
                if ocr % 2 == 0:
                    price += (ocr / 2) * y
                else:
                    price += int(ocr / 2) * y + (ocr % 2) * x
                i += 1
                if i > m-1:
                    break
        print(int(price))