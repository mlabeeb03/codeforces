def solve():
    n = int(input())
    l = list(map(int, input().split()))
    num = int(10E5 + 1)
    arr = [0] * num
    for i in l:
        arr[i] += i
    #print(arr)
    ans = [0] * num
    ans[-1] = arr[-1]
    ans.append(0)
    #print(ans)
    for i in range(num - 2, 0, -1):
        ans[i] = max(arr[i] + ans[i+2], ans[i + 1])
    print(ans[1])
     
for _ in range(1):
    solve()

    