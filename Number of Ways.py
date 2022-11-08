import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")

def solve():
    n = int(input())
    arr = [int(x) for x in input().split()]
    sm = sum(arr)     
    if sm % 3 != 0:
        print(0)
    else:
        tar = sm // 3
        psum = [0]*n
        psum[0] = arr[0]
        for i in range(1,n):
            psum[i] = psum[i-1] + arr[i]
        
        ans = 0
        cnt = 0
        sm = 0
        for i in range(n-1,-1,-1):
            if psum[i] == tar:
                ans += cnt
            if i != n-1 and sm == tar:
                cnt += 1
            sm += arr[i]
            
        print(ans)
   
for _ in range(1):
    solve()