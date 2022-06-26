def solve():
    #n = int(input())
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
          
    print(max(i | m for i in a))
    
for __ in range(int(input())):
    solve()

   