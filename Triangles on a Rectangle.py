# -*- coding: utf-8 -*-

def areaOfTri(base, height):
    return int(2 * (base * (height / 2)))

for i in range(int(input())):
    w, h = map(int, input().split())
    x1 = list(map(int, input().split()))    #the x cords of bottom line, y = 0
    x2 = list(map(int, input().split()))    #the x cords of top line, y = h
    y1 = list(map(int, input().split()))    #the y cords of left line, x = 0
    y2 = list(map(int, input().split()))    #the y cords of right line, x = w
    
    print(max(areaOfTri(x1[-1] - x1[1], h), areaOfTri(x2[-1] - x2[1], h), areaOfTri(y1[-1] - y1[1], w), areaOfTri(y2[-1] - y2[1], w)))
    