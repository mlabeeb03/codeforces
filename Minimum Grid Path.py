import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")

def solve():
    n = int(input())
    arr = list(map(int, input().split()))    
    a = []
    b = []
    for i in range(0, n, 2):
        if i == n - 1:
            a.append(arr[i])
            break
        a.append(arr[i])
        b.append(arr[i + 1])
    amn = a[:]
    bmn = b[:]
    for i in range(1, len(amn)):
        amn[i] = min(amn[i], amn[i - 1])
    for i in range(1, len(bmn)):
        bmn[i] = min(bmn[i], bmn[i - 1])
    apre = a[:]
    bpre = b[:]    
    for i in range(1, len(apre)):
        apre[i] += apre[i - 1]
    for i in range(1, len(bpre)):
        bpre[i] += bpre[i - 1]
   
    ans = a[0] * n + b[0] * n
    
    for i in range(len(bpre)):
        ans = min(ans, (apre[i] - amn[i]) + (bpre[i] - bmn[i]) + (amn[i] + bmn[i]) * (n - i)) 
        try:
            ans = min(ans, (apre[i + 1] - amn[i + 1]) + (bpre[i] - bmn[i]) + amn[i + 1] * (n - (i + 1)) + bmn[i] * (n - i)) 
        except:
            pass
   
    print(ans)
    
for _ in range(int(input())):
    solve()