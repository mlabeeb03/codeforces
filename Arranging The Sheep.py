def solve():
    n = int(input())
    #n, W = map(int, input().split())    
    #a = list(map(int, input().split())) 
    a = list(map(str, input())) 
    she = a.count('*')
    #print(a)
    ans = 10E12
    s = []
    for i in range(n):
        if a[i] == '*':
            s.append(i)
    #print(s)
    for i in range(she // 2 - 1, she // 2 + 1):
        t = 0
        for j in range(i):
            t += s[i] - s[j] - 1 - (i - j - 1)
        for j in range(i + 1, she):
            t += s[j] - s[i] - 1 - (j - i - 1)
        ans = min(ans, t)
    print(max(ans, 0))
            
for _ in range(int(input())):
    solve()

    