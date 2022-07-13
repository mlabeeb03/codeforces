import heapq as hq
def solve():
    n = int(input())
    #n, k = map(int, input().split())    
    a = list(map(int, input().split())) 
    #a = list(map(str, input())) 
    
    arr = []
    tn = n
    for i in range(tn):
        if a[i] > 0:
           hq.heappush(arr, [a[i] * -1, i + 1])
        else:
            n -= 1
            
    ans = 0
    anslist = []
    while arr:
        x = hq.heappop(arr)
        y = None
        try:
            y = hq.heappop(arr)
        except:
            break
        anslist.append([x[1], y[1]])
        ans += 1
        x[0] += 1
        y[0] += 1
        if x[0] < 0:
            hq.heappush(arr, x)
        if y[0] < 0:
            hq.heappush(arr, y)
    print(ans)
    while anslist:
        print(*anslist.pop())
        
for _ in range(int(input())):
    solve()