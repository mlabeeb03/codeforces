import sys
try:
    file = open('inp.txt', 'r')
    input = lambda: file.readline().rstrip("\n\r")
except:
    input = lambda: sys.stdin.readline().rstrip("\n\r")   

def solve():
    n = int(input())
    ans = []
    while n > 1:
        x, y = (n + 1) // 2, (n - 1) // 2
        if x % 2 > 0:
            ans.append('1')
            n = x
        else:
            ans.append('2')
            n = y
    ans.reverse()        
    print("".join(ans))

for _ in range(int(input())):
    solve()


