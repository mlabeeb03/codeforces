import sys
s, m = map(int, input().split())

strr = []
bns = []

for _ in range(m):
    a = list(map(int, input().split()))
    strr.append(a[0])
    bns.append(a[1])
    
for i in range(m):
    for j in range(m):
        if strr[i] < strr[j]:
            strr[i], strr[j] = strr[j], strr[i]
            bns[i], bns[j] = bns[j], bns[i]
            
for i in range(m):
    if s <= strr[i]:
        print('NO')
        sys.exit()
    else:
        s += bns[i]
print('YES')
    

    