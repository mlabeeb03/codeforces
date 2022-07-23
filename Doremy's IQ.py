#import sys
#input = sys.stdin.readline

def solve():
    #n = int(input())
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    ans = [0] * n
    kue = 0
    for i in range(n - 1, -1, -1):   
        if a[i] <= kue:
            ans[i] = 1
        elif a[i] > kue and kue < q:
            ans[i] = 1
            kue += 1
        
    print(''.join(str(i) for i in ans))
    
for _ in range(int(input())):
    solve()