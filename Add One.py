import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")
 
def solve():
    n, m = map(str, input().split())
    a = [int(i) for i in n]
    b = int(m)
    ans = 0
    for i in a:
        ans += arr[b + i] % mod
    print(ans % mod)
 
num = 2000011
mod = 1000000007
arr = [None] * num
arr[0] = 1
dic = [1,0,0,0,0,0,0,0,0,0]
bac = [0,0,0,0,0,0,0,0,0,0]
for i in range(1, num):
    for j in range(2, 10):
        bac[j] = dic[j - 1] % mod
    bac[0] = dic[9] % mod
    bac[1] = (dic[9] + dic[0]) % mod
    arr[i] = sum(bac) % mod
    dic = bac[:]
        
for _ in range(int(input())):
    solve()