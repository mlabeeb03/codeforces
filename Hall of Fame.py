import sys
input = lambda: sys.stdin.readline().rstrip("\n\r")

def solve():
    n = int(input())    
    a = list(map(str, input())) 
    
    if 'R' not in a or 'L' not in a:
        print(-1)
        return
        
    for i in range(n - 1):
        if a[i] == 'L' and a[i + 1] == 'R':
            print(i + 1)
            return
        elif a[i] == 'R' and a[i + 1] == 'L':
            print(0)
            return
    
    print(-1)

for _ in range(int(input())):
    solve()

    