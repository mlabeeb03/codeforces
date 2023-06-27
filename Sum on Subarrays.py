import sys
try:
    file = open('inp.txt', 'r')
    input = lambda: file.readline().rstrip("\n\r")
except:
    input = lambda: sys.stdin.readline().rstrip("\n\r")

def solve():
    n, k = map(int, input().split())
    arr = [-1] * n
    for i in range(n, 0, -1):
        if i <= k:
            arr[i - 1] = 1000
            k -= i
        else:
            if k > 0:
                arr[i - 1] = 901
                k -= 1
                ind = i - 2
                while k > 0:
                    arr[ind] = -1
                    ind -= 1
                    k -= 1
                if ind > -1:
                    arr[ind] = -902
            break
    print(*arr)

for _ in range(int(input())):
    solve()
