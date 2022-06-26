def solve(s, t):
    #n = int(input())
    #n, k = map(int, input().split())
    #a = list(map(int, input().split()))
    #a = list(map(int, input()))
    
    tp = sp = taken = 0
    while(sp < len(s) and tp < len(t)):
        if s[sp] == t[tp]:
            taken += 1
            tp += 1
        sp += 1
    return (len(s) - taken + len(t) - taken)
    
p2 = []
i = 1
while(i <= 2000000000000000000):
    p2.append(str(i))
    i *= 2
for __ in range(int(input())):
    a = input()
    ans = len(a) + 1
    for i in p2:
        ans = min(ans, solve(a, i))
    print(ans)

   