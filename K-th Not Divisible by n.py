def solve():
    #n = int(input())
    #a = list(map(int, input().split()))
    n, k = map(int, input().split())
    
    print(k + ((k - 1) // (n - 1)))
    
    
for t in range(int(input())):
	solve()
