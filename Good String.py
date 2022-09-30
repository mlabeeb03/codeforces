from collections import Counter

def solve():
    #n = int(input())
    l = list(map(int, input()))
    n = len(l)
    
    lst = [[]for i in range(num)]
    for i in l:
        for j in range(10):
            if len(lst[i * 10 + j]) == 0 or lst[i * 10 + j][-1] != i:
                lst[i * 10 + j].append(i)
        for j in range(num//10):
            if len(lst[j * 10 + i]) == 0 or lst[j * 10 + i][-1] != i:
                lst[j * 10 + i].append(i)
    mx = 0
    for i in range(num):
        if len(lst[i]) > 1:
            if lst[i][0] == lst[i][-1]:
                mx = max(mx, len(lst[i]) - 1)
            else:
                mx = max(mx, len(lst[i]))
    a = Counter(l)
    for i in a.values():
        mx = max(mx, i)
    
    print(n - mx)
    
num = 100
for _ in range(int(input())):
    solve()

    