def solve():
    s = list(map(str, input()))
    t = list(map(str, input()))
    
    slen, tlen = len(s), len(t)
    si, ti = slen - 1, tlen - 1
    count = 0
    while si >= 0 and ti >= 0:
        if s[si] == t[ti]:
            si -= 1
            ti -= 1
            count += 1
            if count == tlen:
                print('YES')
                return
        else:
            si -= 2
    print('NO')
 
for _ in range(int(input())):
    solve()
