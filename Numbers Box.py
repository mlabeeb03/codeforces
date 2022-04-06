import math
for _ in range(int(input())):
    n, m = map(int, input().split())
    arr = [] 
    x = 0
    for _ in range(n):
        row = list(map(int, input().split()))
        arr.append(row)
        row = [_ for _ in row if _ < 0]
        x += len(row)
        
    sum = 0
    minn = math.inf    
    for i in range(n):
        for j in range(m):
            k = abs(arr[i][j])
            sum += k
            if k < minn:
                minn = k
    if x % 2 == 0:
        print(sum)
    else:
        print(sum - minn*2)

    