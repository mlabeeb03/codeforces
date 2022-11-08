import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")
 
def solve():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    even = 0
    odd = 0
    sm = sum(a)
    for i in range(n):
        if a[i] % 2 == 0:
            even += 1
        else:
            odd += 1
    for i in range(q):
        #print(even, odd)
        t, j = map(int, input().split())
        if t == 0:
            sm += (j * even)
            print(sm)
            if j % 2 == 1:
                odd += even
                even = 0
        else:
            sm += (j * odd)
            print(sm)
            if j % 2 == 1:
                even += odd
                odd = 0
                
                                   
for _ in range(int(input())):
    solve()