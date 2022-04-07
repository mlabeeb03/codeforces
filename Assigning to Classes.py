for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    x = arr[n-1] - arr[n]
    print(abs(x))


        

    