for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        a[i] -= i+1
    arr = [0 for _ in range(n*2)]
    for i in range(n):
        arr[a[i]+n] += 1
    for i in range(n*2):
        ans += (arr[i] * (arr[i]-1))/2
    print(int(ans))



