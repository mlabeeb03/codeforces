import sys
input = lambda: sys.stdin.readline().rstrip("\n\r")
#file = open('inp.txt', 'r') ; input = lambda: file.readline().rstrip("\n\r")

def solve():
    n, x, y = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(n):
        if a[i] > y:
            a[i] = y
    ans = 0
    #print(a)
    for i in range(n):
        #print('i x ans: ', i, x, ans)
        if a[i] <= x:
            x += 1
            ans += 1
            if x == y: print(ans); return
        else:
            inc = i - (n - i)
            if inc <= 0: 
                print(-1)
                return
            elif x + inc >= y:
                x -= (n - i)
                ans += (n - i)
                for j in range(n):
                    x += 1
                    ans += 1
                    if x == y:
                        print(ans)
                        return
            else:
                diff = a[i] - x
                t = diff // inc
                x += t * inc
                ans += t * n
                #print('diff inc t x ans:', diff, inc, t, x, ans)
                if x == y:
                    print(ans)
                    return
                if x >= a[i]:
                    x += 1
                    ans += 1
                    if x == y:
                        print(ans)
                        return
                else:
                    x -= n - i
                    ans += n - i
                    if x + i + 1 >= y:
                        for j in range(i + 1):
                            x += 1
                            ans += 1
                            if x == y:
                                print(ans)
                                return
                    else:
                        x += i + 1
                        ans += i + 1
                #print('here', i, x, ans)
                
    t = ((y - x) // n) * n
    x += t
    ans += t
    if x >= y:
        print(ans)
        return
    for i in range(n):
        x += 1
        ans += 1
        if x >= y:
            print(ans)
            return
    
for _ in range(int(input())):
    solve()