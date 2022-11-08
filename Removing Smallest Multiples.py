import sys
input = lambda: sys.stdin.readline().rstrip("\r\t")

def solve():
    n = int(input())
    a = list(map(int, input().rstrip("\n\r\t")))
    ans = 0
    for i in range(n):
        if a[i] == 0 or a[i] == -1:
            for j in range(i, n, i + 1):
                if a[j] == 1:
                    break
                elif a[j] == 0:
                    ans += i + 1
                    a[j] = -1
    print(ans)
       
for _ in range(int(input())):
    solve()
    
    

    