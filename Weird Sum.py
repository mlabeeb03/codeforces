import sys
input = sys.stdin.readline
 
def solve():
    n, m = map(int, input().split())
    nums = [[] for i in range(100001)]
    for i in range(n):
        row = list(map(int, input().split()))
        for j in range(m):
            nums[row[j]].append((i + 1, j + 1))
    ans = 0
    for i in nums:
        x = len(i)
        if x > 0:
            sumlist = [i[-1][0]] * x
            for j in range(x - 2, -1, -1):
                sumlist[j] = sumlist[j + 1] + i[j][0]
                ans += sumlist[j + 1] - (i[j][0] * (x - (j + 1)))
            i.sort(key = lambda t:t[1])
            sumlist = [i[-1][1]] * x
            for j in range(x - 2, -1, -1):
                sumlist[j] = sumlist[j + 1] + i[j][1]
                ans += sumlist[j + 1] - (i[j][1] * (x - (j + 1)))    
    print(ans)
    
for _ in range(1):
    solve()