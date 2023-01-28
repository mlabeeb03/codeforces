from sys import stdin
input=lambda :stdin.readline()[:-1]

inf=10**18
def calc(a,b,n,m,mid):
  res=0
  if mid!=n-1:
    for i in range(mid+1):
      res+=b[i]
    if res<=m:
      return True
  res=a[mid]
  flag=False
  cnt=0
  now=0
  while cnt<mid-1:
    if flag==False and b[now]==a[mid]:
      flag=True
      now+=1
    else:
      res+=b[now]
      cnt+=1
      now+=1
  return res<=m

def solve():
  n,m=map(int,input().split())
  a=list(map(int,input().split()))
  b=sorted(a)
  ng,ok=n,-1
  while abs(ng-ok)>1:
    mid=(ng+ok)//2
    if calc(a,b,n,m,mid):
      ok=mid
    else:
      ng=mid
  print(n-ok)
  
    

for _ in range(int(input())):
  solve()