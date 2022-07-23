import sys
input = sys.stdin.readline

from collections import Counter

def solve():
    n, k = map(int, input().split())   
    a = list(map(int, input().split()))
    dic = Counter(a)
    if len(dic) > k:
        print(-1)
        return
    if k == n:
        print(n)
        print(*a)
        return
    arr = []
    for i in dic.keys():
        arr.append(i)
    for i in range(k - len(dic)):
        arr.append(arr[-1])
    print(len(arr) * n)
    print(*arr * n)
    
for _ in range(int(input())):
    solve()
    