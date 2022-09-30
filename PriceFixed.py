import copy
def solve():
    n = int(input())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    a.sort(key=lambda x: x[1], reverse = True)
    tot = sum(i[0] for i in a)
    l = tot
    r = tot * 2
    ans = tot * 2
    while(l <= r):
        m = (l + r) // 2
        num2 = m - tot
        taken = 0
        index = 0
        leftati = 0
        for i in range(n):
            index = i
            if num2 >= a[i][0]:
                taken += a[i][0]
                num2 -= a[i][0]
                leftati = 0
            else:
                taken += num2                
                leftati = a[i][0] - num2
                break
        good = 1
        for i in range(n - 1, index, -1):
            if a[i][1] > taken:
                good = 0
                break
            else:
                taken += a[i][0]
        if a[index][1] > taken and leftati > 0:
            good = 0
        if good == 1:
            ans = m
            r = m - 1
        else:
            l = m + 1
    print(ans)
            
for _ in range(1):
    solve()

    