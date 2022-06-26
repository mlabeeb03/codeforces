def solve():
    n = int(input())
    a = list(map(int, input().split()))
    #n, k = map(int, input().split())
    
    if a[0] == 0 and len(set(a)) == 1:
        print(0)
        return
    
    arr = [a[0]]
    for i in range(1, n):
        if a[i] == arr[-1]:
            continue
        arr.append(a[i])
    
    x = arr[1: -1].count(0)
    if x == 0:
        print(1)
    else:
        print(2)
           
for t in range(int(input())):
	solve()
