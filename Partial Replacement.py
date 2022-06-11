def solve():
    n, k = map(int, input().split())
    s = list(map(str, input()))
    
    start = s.index('*') 
    s[start] = 'x'
    cnt = s.count('*')
    ans = 1
    if cnt > 0:
        end = n - s[::-1].index('*') - 1
        s[end] = 'x'
        cnt -= 1
        ans += 1
    if cnt > 0:   
        while(start + k < end):
            x = start + k
            while(s[x] != '*'):
                if s[x] == 'x':
                    print(ans)
                    return
                x -= 1
            s[x] = 'x'
            ans += 1
            start = x
    print(ans)

for _ in range(int(input())):
    solve()

    