import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")

def solve():
    n = int(input())
    a = list(map(int, input()))
    if n < 1001:
        s = -1
        for i in range(n):
        	if a[i] == 1:
        		s = i
        		break
        if s == -1:
            print(0)
            return
        u = int("".join(str(x) for x in a), 2)
        v = 0
        ans = 0
        for i in range(s, n):
            v = v * 2 + a[i]
            ans = max(ans, u | v)
        print(format(ans, '0' + str(n - s) + 'b'))
    else:
        s = a.index(1)
        u = int("".join(str(x) for x in a), 2)
        temp = []
        for i in range(100):
            temp.append(a.pop())
        v = int("".join(str(x) for x in a), 2)
        for i in range(100):
            a.append(temp.pop())
        ans = 0
        for i in range(n - 100, n):
            v = v * 2 + a[i]
            ans = max(ans, u | v)
        print(format(ans, '0' + str(n - s) + 'b'))
        
for _ in range(1):
    solve()

    