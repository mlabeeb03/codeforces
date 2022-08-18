#import sys
#input = sys.stdin.readline

def solve():
    #n = int(input())
    #n, k = map(int, input().split())
    #a = list(map(int, input().split()))
    a = list(map(int, input()))
    l = len(a)
    x = []
    y = []
    i = j = 0
    for i in range(0, l, 2):
        x.append(a[i])
    for i in range(1, l, 2):
        y.append(a[i])
    if x:   
        i = int(''.join(str(t) for t in x))
    if y:
        j = int(''.join(str(t) for t in y))
    
    print((i + 1) * (j + 1) - 2)

       
for _ in range(int(input())):
    solve()

    