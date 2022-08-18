#import sys
#input = sys.stdin.readline

def solve():
    n = int(input())
    #n, k = map(int, input().split())
    a = list(map(int, input().split()))
    dic = {}
    fa, ca = 0, 0
    for i in range(n):
        if a[i] in dic:
            ca += dic[a[i]]
        else:
            dic[a[i]] = 0
        dic[a[i]] += i + 1
        fa += ca
    print(fa)
    
for _ in range(int(input())):
    solve()

    