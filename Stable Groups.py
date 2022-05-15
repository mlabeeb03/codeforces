import math
#for _ in range(int(input())):
#n = int(input())
n,k,x = map(int, input().split())
a = list(map(int, input().split()))
#a = list(map(int, input()))
a.sort()
lst = []
ans = 2
for i in range(n-1):
    if a[i+1]-a[i] > x:
        lst.append(a[i+1] - a[i])
        ans += 1
lst.sort()
ind = 0
while(ind < len(lst) and k >= math.ceil(lst[ind]//x) - 1):
    k -= math.ceil(lst[ind]//x) - 1
    lst[ind] = 0
    ind += 1
    ans -= 1
print(ans)

    
    
    
    


