import math
for _ in range(int(input())):
    n = int(input())
    ans = []
    k = math.ceil(math.log(n, 2))
    cutter = 2**(k-1)
    for i in range(cutter - 1, -1, -1):
        ans.append(i)
    for i in range(cutter, n):
        ans.append(i)
    print(*ans)
    

    