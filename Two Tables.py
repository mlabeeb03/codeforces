def solve():
    X, Y = map(int, input().split())
    x1, y1, x2, y2 = map(int, input().split())
    w, h = map(int, input().split())
    
    b = 0 if h <= y1 else h - y1
    t = 0 if h <= Y - y2 else y2 - (Y - h)
    l = 0 if w <= x1 else w - x1
    r = 0 if w <= X - x2 else x2 - (X - w)
    
    if w + (x2 - x1) > X and h + (y2 - y1) > Y:
        print(-1)
    elif w + (x2 - x1) <= X and h + (y2 - y1) <= Y:
        print(min(b, t, l ,r))
    elif h + (y2 - y1) <= Y:
        print(min(t, b))
    else:   
        print(min(l ,r))
        
for _ in range(int(input())):
    solve()