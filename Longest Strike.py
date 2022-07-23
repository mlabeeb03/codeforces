from collections import Counter
t=int(input())
for w in range (t):
    n,k=map(int,input().split())
    arr=list(map(int,input().split()))
    arr = Counter(arr)
    ks = []
    for i in arr.keys():
        if arr[i] >= k:
            ks.append(i)
    arr = ks
    
    
    l = len(arr)
    if l == 0:
        print(-1)
        continue 
    arr.sort()
    if(len(arr)==0):
        print("-1")
        continue
    l=arr[0]
    r=arr[0]
    ansL=l
    ansR=r
    for val in arr:
        if(val-r==1):
            r=val
        else :
            if( r-l>ansR-ansL):
                ansL=l
                ansR=r
            l=val
            r=val
    if( r-l>ansR-ansL):
        ansL=l
        ansR=r
 
    print(ansL, ansR)