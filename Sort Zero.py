import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")
import math
def solve():
    n = int(input())
    #n, k = map(int, input().split())  
    a = list(map(int, input().split()))
    dic = {}
    num = 0
    for i in range(n):
        if a[i] in dic:
            dic[a[i]][0] += 1
            dic[a[i]][2] = i
        else:
            dic[a[i]] = [1, i, i]
            num += 1
    ans = num
    i = n - 1
    mn = math.inf
    while ans > 0:
        if a[i] < mn and dic[a[i]][0] == dic[a[i]][2] - dic[a[i]][1] + 1:
            ans -= 1
            mn = a[i]
            i -= dic[a[i]][2] - dic[a[i]][1] + 1
            #print(i, mn, a[i])
        else:
            break
    #print(dic)
    print(ans)
    #print()
            
        
for _ in range(int(input())):
    solve()
# dic = {key: [count, first index, last index]}