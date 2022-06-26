def solve():
    n = int(input())
    #n, m = map(int, input().split())
    a = list(map(int, input().split()))
    #a = list(map(int, input()))
    
    a.sort()
    sums = [a[0]]
    for i in range(1, n + 2):
        sums.append(a[i] + sums[i - 1])
    
    if sums[n - 1] == a[n] or sums[n - 1] == a[n + 1]:
        print(*a[:n])
        return
    
    w1 = [sums[-2] - i for i in a[:n]]
    w2 = [sums[-1] - i for i in a[:n]]
    for i in range(n):
        if w1[i] == a[-1]:
            print(*a[:i], *a[i + 1: n], a[n])
            return
        if w2[i] == a[-2]:
            print(*a[:i], *a[i + 1: n], a[n + 1])
            return
    
    print(-1)
      
for __ in range(int(input())):
    solve()

   