import sys
input = sys.stdin.readline
 
def solve():
    n = int(input())
    #a = list(map(int, input().split()))
    ans = 2520
    for i in range(n, ans + ans * (n // ans) + 1):
        fine = 1
        a = [int(x) for x in str(i) if x != '0']
        for j in a:
            if i % j != 0:
                fine = 0
                break
        if fine == 1:
            print(i)
            break
    
for _ in range(int(input())):
    solve()