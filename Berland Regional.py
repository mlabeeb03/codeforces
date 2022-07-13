def solve():
    n = int(input())
    #a, b, k = map(int, input().split())    
    u = list(map(int, input().split())) 
    s = list(map(int, input().split())) 
    #a = list(map(str, input())) 
    
    arr = []
    arrlen = [0] * (n + 1)
    for _ in range(n + 1):
        arr.append([])
    t = sorted(zip(s, u), reverse=True)
    for i in range(n):
        arrlen[t[i][1]] += 1
        if arrlen[t[i][1]] == 1:
            arr[t[i][1]].append(t[i][0])
        else:
            arr[t[i][1]].append(t[i][0] + arr[t[i][1]][arrlen[t[i][1]] - 2])
    
    ans = [0] * (n + 1)
    for i in range(1, n + 1):
        for k in range(1, arrlen[i] + 1):
            ans[k] += arr[i][arrlen[i] - arrlen[i] % k - 1]
    print(*ans[1:])
        
for _ in range(int(input())):
    solve()