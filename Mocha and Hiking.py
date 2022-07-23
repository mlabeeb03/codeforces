t=int(input())
for _ in range(t):
  n=int(input())
  a=list(map(int,input().split()))
  zc=a.count(0)
  if n==1 and a[0]==1:
    print(2,1)
  elif zc==0:
    ans=[n+1]
    for i in range(1,n+1):
      ans.append(i)
    print(*ans)
  else:
    if a[-1]==0:
      ans=[]
      for i in range(1,n+2):
        ans.append(i)
      print(*ans)
    else:
      zind=0
      oind=0
      for i in range(1,len(a)):
        if a[i]==1 and a[i-1]==0:
          zind=i
          oind=i+1
      ans=[]
      for i in range(1,oind):
        ans.append(i)
      ans.append(n+1)
      for i in range(oind,n+1):
        ans.append(i)
      print(*ans)