import sys
input = sys.stdin.readline
def get(x):
    if x == 0:
        return 0
    elif x // 10 == 0:
        return x
    else:
        i = 10
        t = 2
        while i < 1000000001:
            if x // 10 < i:
                return ((x // i) * int('1' * t)) + get(x % i)
                break
            i *= 10
            t += 1

def solve():
    l, r = map(int, input().split())   
    print(get(r) - get(l))
    
    
for _ in range(int(input())):
    solve()
    