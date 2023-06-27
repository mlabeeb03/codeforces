import sys
try:
    file = open('inp.txt', 'r')
    input = lambda: file.readline().rstrip("\n\r")
except:
    input = lambda: sys.stdin.readline().rstrip("\n\r")

def solve():
    #n = int(input())
    #a, b, c= map(int, input().split())
    #a = list(map(int, input().split()))
    a = [i for i in input()]
    i = j = 0
    for x in a:
        if x == 'U':
            i -= 1
        elif x == 'D':
            i += 1
        elif x == 'L':
            j -= 1
        elif x == 'R':
            j += 1
    print(abs(i)+abs(j))
    

for _ in range(int(input())):
    solve()
