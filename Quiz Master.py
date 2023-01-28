import sys
input = lambda: sys.stdin.readline().rstrip("\n\r")
from math import inf

def solve():
    n, m = list(map(int, input().split()))
    a = (list(map(int, input().split())))
    a.sort()   
 
    dic = {}
    notavb = set()
    for i in range(1, m + 1): 
        dic[i] = 0   
        notavb.add(i)
      
    ans = inf
    l, r = 0, 0
    for i in facts[a[r]]:
        if i <= m:
            dic[i] += 1
            if i in notavb:
                notavb.remove(i)
    while r < n:      
        if len(notavb) == 0:
            ans = min(ans, a[r] - a[l])
            for i in facts[a[l]]:
                if i <= m:
                    dic[i] -= 1
                    if dic[i] == 0:
                        notavb.add(i)
            l += 1
            r = max(r, l)
        else:
            r += 1
            if r < n:
                for i in facts[a[r]]:
                    if i <= m:
                        dic[i] += 1
                        if i in notavb:
                            notavb.remove(i)
    print(-1 if ans == inf else ans)

num = 100001
facts = [set([i]) for i in range(num + 1)]
for i in range(1, num // 2 + 1):
    ind = 1
    while i * ind <= num:
        facts[i * ind].add(i)
        ind += 1
#for i in facts: print(i)
for _ in range(int(input())):
    solve()