def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    
    ans = ['B'] * m
    for i in range(n):
        if a[i] < m + 1 - a[i] and ans[a[i] - 1] == 'B':
            ans[a[i] - 1] = 'A'
        elif a[i] >= m + 1 - a[i] and ans[m - a[i]] == 'B':
            ans[m - a[i]] = 'A'
        elif ans[a[i] - 1] == 'B':
            ans[a[i] - 1] = 'A'
        else:
            ans[m - a[i]] = 'A'       
    
    print(''.join(ans))       

for _ in range(int(input())):
    solve()