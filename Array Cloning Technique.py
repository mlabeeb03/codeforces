from collections import Counter
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = a[:]
    c = a[:]
    
    if len(set(b)) == 1:
        print(0)
    elif len(set(b)) == n:
        x = 0
        i = 1
        while(i-1 < n-1):
            i *= 2
            x += 1
        print(n-1+x)
    else:
        high = Counter(a)
        t = high.most_common(1)[0][1]
        x = 1
        i = t*2
        while(i-t < n-t):
            i *= 2
            x += 1        
        print(n-t+x)
    