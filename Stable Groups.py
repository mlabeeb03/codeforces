n,k,x = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
lst = []
for i in range(n-1):
    if a[i+1]-a[i] > x:
        lst.append(a[i+1] - a[i])
lst.sort(reverse=True)
for i in range(len(lst)-1, -1, -1):
    if (lst[i]-1)//x <= k:
        k -= (lst[i]-1)//x
        lst.pop()
print(len(lst) + 1)
    