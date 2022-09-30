import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")
 
def solve():
    #n = int(input())
    n, m = map(int, input().split())
    #a = list(map(int, input().split()))
    
    if n == 1 or m == 1:
        print(n, m)
        return
    if n == 2 and m == 2:
        print(n, m)
        return
    if n == 2 and m == 3:
        print(2, 2)
        return
    if n == 3 and m == 2:
        print(2, 2)
        return
    if n == 3 and m == 3:
        print(2, 2)
        return
        
    print(n, m)
        
for _ in range(int(input())):
    solve()