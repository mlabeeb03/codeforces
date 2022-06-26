def solve():
    #n = int(input())
    n, m = map(int, input().split())
    #a = list(map(int, input().split()))
    #a = list(map(int, input()))    
    #arr = [input() for _ in range(n + n - 1)]
    
    ans = [0] * m 
    for i in range(n + n - 1):
        x = input()
        for j in range(m):
            ans[j] ^= ord(x[j])
            
    print(''.join(chr(i) for i in ans))
for __ in range(int(input())):
    solve()

   