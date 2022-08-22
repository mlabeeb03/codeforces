def solve():
    s = input()
    t = input()
    n = len(s)
    m = len(t)
    ans = False
    for i in range(n):
        if s[i] == t[0]:
            for j in range(0, n - i):
                if t == s[i: i + j + 1] + s[max(0,(i + j) - (m - (j + 1))): i+j][::-1]:
                    ans = True
    print('YES' if ans else 'NO')

for __ in range(int(input())):
    solve()