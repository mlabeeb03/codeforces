import sys
input = sys.stdin.readline

from collections import Counter

def solve():
    n = int(input())
    a = []
    one = [[] for i in range(11)]
    two = [[] for i in range(11)]
    for i in range(n):
        a.append([ord(x) - 97 for x in list(map(str, input()))])
    for i in range(n):
        one[a[i][0]].append(a[i][1])
        two[a[i][1]].append(a[i][0])
    ans = 0
    for i in range(11):
        l = len(one[i])
        if l > 0:
            ans += (l * (l - 1)) // 2
            dic = Counter(one[i])
            for x in dic.values():
                ans -= (x * (x - 1)) // 2
        l = len(two[i])
        if l > 0:
            ans += (l * (l - 1)) // 2
            dic = Counter(two[i])
            for x in dic.values():
                ans -= (x * (x - 1)) // 2
    print(ans)   
    
for _ in range(int(input())):
    solve()
    