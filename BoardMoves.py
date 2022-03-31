tcs = int(input())
for i in range(tcs):
    n = int(input())
    res = 0
    for i in range(1,int(n / 2)+1):
        res += i * i
    print(res*8)

