import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")

def solve():
    n, c, q = map(int, input().split())    
    s = list(map(str, input()))
    
    left = [0] * (c + 1)
    right = [0] * (c + 1)
    diff = [0] * (c + 1)
    left[0] = 0
    right[0] = n
    for i in range(1, c + 1):
        l, r = map(int, input().split())  
        l -= 1
        r -= 1
        left[i] = right[i - 1]
        right[i] = left[i] + (r - l + 1)
        diff[i] = left[i] - l
    for i in range(q):
        k = int(input())
        k -= 1
        for j in range(c, 0, -1):
            if k < left[j]:
                continue
            else:
                k -= diff[j]
        print(s[k])

for _ in range(int(input())):
    solve()

    