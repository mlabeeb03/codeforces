from collections import Counter
n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

i1=[None]*n
i2=[None]*n
dif1=[None]*n
dif2=[None]*n

for i in range(n):
    i1[a[i] - 1] = i
    i2[b[i] - 1] = i
    
for i in range(n):
    dif1[i]=i1[i]-i2[i]
    dif2[i]=i1[i]-i2[i]
    
for i in range(n):
    if dif1[i] > 0:
        dif1[i] -= n
    if dif2[i] < 0:
        dif2[i] += n
x = (max(list(Counter(dif1).values())))
y = (max(list(Counter(dif2).values())))
print(max(x, y))
  