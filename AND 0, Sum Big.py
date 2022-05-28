def solve():
    n, k = map(int, input().split())    
    print((pow(n,k))%1000000007)

for _ in range(int(input())):
    solve()

    