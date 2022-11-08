import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")

def calc(arr):
    intim = 0
    for i in range(1, 4):
        if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
            intim += 1
        elif arr[i] < arr[i - 1] and arr[i] < arr[i + 1]:
            intim += 1
    return intim

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    if n < 3:
        print(0)
        return
    arr = [a[0]] + a + [a[-1]]
    sta = [0] * (n + 2)
    for i in range(1, n + 1):
        if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
            sta[i] = 1
        elif arr[i] < arr[i - 1] and arr[i] < arr[i + 1]:
            sta[i] = -1
    intim = n - (sta.count(0) - 2)
    ans = n
    for i in range(2, n):
        vals1 = arr[i - 2: i + 3]
        vals2 = arr[i - 2: i + 3]
        vals2[2] = vals2[3]
        vals3 = arr[i - 2: i + 3]
        vals3[2] = vals3[1]
        int1 = calc(vals1)
        int2 = calc(vals2)
        int3 = calc(vals3)
        ans = min(ans, intim - (int1 - int2), intim - (int1 - int3))
    print(ans)
                                   
for _ in range(int(input())):
    solve()
