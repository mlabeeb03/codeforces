for _ in range(int(input())):
    n = k = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    a.sort(reverse=True)
    b.sort(reverse=True)
    res = 0  
 
    ind = k - (k//4)
    asum = sum(a[0: ind])
    bsum = sum(b[0: ind])
    bind = ind
    aind = ind - 1
    initk = k//4
    
    while(asum < bsum):
        res += 1
        k += 1
        asum += 100
        if k//4 == initk:
            if bind < n:
                bsum += b[bind]
                bind += 1
        else:
            initk = k//4
            if aind > -1:
                asum -= a[aind]
                aind -= 1           
    print(res)   
'''   
while(sum(a[:(n - (n//4))]) < sum(b[:(n - (n//4))])):
    a = [100] + a
    b.append(0)
    n += 1
    res += 1
print(res)
'''
    
