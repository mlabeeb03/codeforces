import sys
input = lambda: sys.stdin.readline().rstrip("\n\r")
#file = open('inp.txt', 'r') ; input = lambda: file.readline().rstrip("\n\r")

def solve():
    n = int(input()) 
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    ai = n - 1
    bi = n - 1
    while ai >= 0:
        if a[ai] == b[bi]:
            bi -= 1
        ai -= 1
    print(bi + 1)
    
for _ in range(int(input())):
    solve()