from operator import itemgetter
for _ in range(int(input())):
    n = int(input())
    a = [int(item) for item in input().split()]
    b = [int(item) for item in input().split()]
    
    odd = []
    for i in range(n):
        odd.append([a[i], i])
    odd.sort(key = itemgetter(0))
    
    l = []
    j = 1
    for i in range(n):
        while b[i] > j:
            l.append([i, odd[j // 2][1]])
            j += 2
            
    ans = 2 * n
    for i in l:
        ans = min(ans, i[0] + i[1])
    print(ans)
    