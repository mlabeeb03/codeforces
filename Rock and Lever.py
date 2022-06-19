def solve():
    n = int(input())
    #n, l, r = map(int, input().split())
    a = list(map(int, input().split()))
    bits = [0] * 32
    
    for i in a:
        bits[i.bit_length()] += 1
    
    ans = 0
    for i in bits:
        ans += (i * (i - 1)) // 2
        
    print(ans)

for __ in range(int(input())):
    solve()