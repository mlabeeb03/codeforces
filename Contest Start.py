for i in range(int(input())):
    n, x, t = map(int, input().split())
    p = min(n, t//x)
    ans = p*(p-1)//2 + p*(n-p)
    print(ans)
        
    