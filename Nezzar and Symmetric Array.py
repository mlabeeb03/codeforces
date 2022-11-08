import sys
input = lambda: sys.stdin.readline().rstrip("\r\t")

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse = True)
    if len(set(a)) != n:
        print('no')
        return
    if len(set(a)) == 1 and a[0] % 2 == 1:
        print('no')
        return
    for i in range(0, 2 * n, 2):
        if a[i] != a[i + 1]:
            print('no')
            return
    curr = 0
    q = n
    for i in range(0, n * 2, 2):
        if a[i] - curr <= 0 or (a[i] - curr) % q > 0 or ((a[i] - curr) // q) % 2 > 0:
            print('no')
            return
        curr += (a[i] - curr) // q
        q -= 1
                
    print('yes')
    
for _ in range(int(input())):
    solve()
    

    