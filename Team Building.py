import sys
try:
    file = open('inp.txt', 'r')
    input = lambda: file.readline().rstrip("\n\r")
except:
    input = lambda: sys.stdin.readline().rstrip("\n\r")

def pos(cap, nocap, l, r):
    if cap == 0:
        return False
    team = [1] * cap
    n = cap
    ind = 0
    while nocap:
        team[ind] += 1
        nocap -= 1
        ind += 1
        if ind == n:
            ind = 0
    for i in team:
        if i < l or i > r:
            return False
    return True   

def solve():
    n, l, r = map(int, input().split())
    a = [int(i) for i in input()]
    cap = a.count(1)
    nocap = a.count(2)
    both = a.count(3)
    # print(cap, nocap, both)
    for i in range(both + 1):
        if pos(cap+i, nocap + (both - i), l, r):
            print('YES')
            return
    
    print('NO')
    
    

for _ in range(int(input())):
    solve()
