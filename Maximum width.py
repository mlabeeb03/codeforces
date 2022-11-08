import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")

def solve():
    slen, tlen = map(int, input().split())
    s = list(map(str, input()))
    t = list(map(str, input()))
    
    fpos = [None] * tlen
    lpos = [None] * tlen   
    si, ti = 0, 0
    while si < slen and ti < tlen:
        if s[si] == t[ti]:
            fpos[ti] = si
            ti += 1
        si += 1
    si, ti = slen - 1, tlen - 1
    while si > -1 and ti > -1:
        if s[si] == t[ti]:
            lpos[ti] = si
            ti -= 1
        si -= 1
        
    ans = 0
    for i in range(tlen - 1, 0, -1):
        ans = max(ans, lpos[i] - fpos[i - 1])
    print(ans)
      
for _ in range(1):
    solve()