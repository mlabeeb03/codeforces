for _ in range(int(input())):
    n = int(input())
    l = [[0,0,0,0,0,None,None,None,None,None] for __ in range(n)]
    ans = 0
    for num in range(n):
        for i in list(map(str, input())):
            l[num][ord(i) - 97] += 1
        s = sum(l[num][:5])
        for i in range(5):
            l[num][i + 5] = l[num][i] - (s - l[num][i])
    for i in range(5):
        l.sort(key = lambda x:x[i + 5], reverse = True)
        #print(l)
        t = 0
        for j in range(n):
            if t + l[j][i + 5] > 0:
                t += l[j][i + 5]
                ans = max(ans, j + 1)
            else:
                break
    print(ans)
        
            