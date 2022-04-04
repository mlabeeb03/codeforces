for i in range(int(input())):
    n = int(input())
    b = list(map(int, input().split()))
    
    dic = {}
    for i in range(n):
        dic[i] = b[i]
    z = list(dic.values())
    dic = {k: v for k, v in sorted(dic.items(), key = lambda item: item[1], reverse = True)}
    x = list(dic.values())
    y = list(dic.keys())
    ans = [0] * n

    cor = 1    
    for i in range(n):
        val = x[i]
        ind = y[i]
        ans[y[i]] = cor
        cor *= -1
        if cor > 0:
            cor += 1

    sum = 0
    for i in range(n):
        sum += 2 * abs(ans[i]) * z[i]
    
    print(sum)
    print(0, end = " ")
    print(*ans)
 