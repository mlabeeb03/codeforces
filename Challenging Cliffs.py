for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    m = 1000000000
    mind = 0
    for i in range(n-1):
        if a[i+1] - a[i] < m:
            m = a[i+1] - a[i]
            mind = i
    print(a[mind], end=" ")
    for i in range(mind+2, n):
        print(a[i], end=" ")
    for i in range(mind):
        print(a[i], end=" ")
    print(a[mind+1])


