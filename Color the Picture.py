import sys
input = sys.stdin.readline

def solve():
    #n = int(input())
    r, c, k = map(int, input().split())    
    a = list(map(int, input().split()))
    a.sort(reverse = True)
    
    if a[0] >= r * c:
        print('Yes')
        return
    
    req = c
    rowise = a[:]
    done = [0] * k
    for i in range(k):
        if rowise[i] // r > 1 and req > 1:
            rowise[i] -= r * 2
            req -= 2
            done[i] = 1
            if req == 0:
                print('Yes')
                return
    for i in range(k):
        if rowise[i] // r > 0:
            if (rowise[i] // r == 1 and done[i] == 0) or (req == 1 and done[i] == 0):
                continue
            req -= rowise[i] // r
            if req < 1:
                print('Yes')
                return
            
    req = r
    colwise = a[:]
    done = [0] * k
    for i in range(k):
        if colwise[i] // c > 1 and req > 1:
            colwise[i] -= c * 2
            req -= 2
            done[i] = 1
            if req == 0:
                print('Yes')
                return
            
    for i in range(k):
        if colwise[i] // c > 0:
            if (colwise[i] // c == 1 and done[i] == 0) or (req == 1 and done[i] == 0):
                continue
            req -= colwise[i] // c
            if req < 1:
                print('Yes')
                return
            
    print('No')

for _ in range(int(input())):
    solve()

    