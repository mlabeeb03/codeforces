import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")
from collections import Counter

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    lst = sorted(list(Counter(a).values()))
    dic = Counter(lst) 
    l = max(lst)
    
    #print(lst)
    #print(dic)
    
    presum = [0] * (l + 1)
    for i in range(1, l + 1):
        if i in dic:
            presum[i] = presum[i - 1] + dic[i] * i
        else:
            presum[i] = presum[i - 1]
            
    #print(presum)
    
    baray = [presum[-1]] * (l + 1)
    for i in range(1, l + 1):
        if i in dic:
            baray[i] = presum[-1] - presum[i]
        else:
            baray[i] = baray[i - 1]
     
    #print(baray)
    
    cnt = [0] * (l + 1)
    for i in range(l - 1, -1, -1):
        if i + 1 in dic:
            cnt[i] = dic[i + 1] + cnt[i + 1]
        else:
            cnt[i] = cnt[i + 1]
    
    #print(cnt)
    
    ans = baray[0]
    for i in range(1, l + 1):
        ans = min(ans, presum[i - 1] + baray[i] - i * cnt[i])
    print(ans)    
    #print()
    
    
for _ in range(int(input())):
    solve()