for _ in range(int(input())):
    n,k=map(int,input().split())
    ans=[]
    n1=n
    n=[int(el) for el in str(n)]

    p=len(n)
    if k==1:
        for i in range(1,10):
            ans.append(int(str(i)*(p)))
        ans.sort()
        for el in ans:
            if el>=n1:
                res=el
                break
        print(res)
    else :
        for i in range(1,10):
            ans.append(int(str(i)*(p)))
        ans.sort()
        for el in ans:
            if el>=n1:
                res=el
                break
        for i in range(0,10):
            for j in range(i+1,10):
                ok=True
                for ind in range(len(n)):
                    if n[ind]<j:
                        t=n[:]
                        if n[ind]<i:
                            t[ind]=i
                        else:
                            t[ind]=j  
                        for o in range(ind+1,len(n)):
                            t[o]=i
                        t="".join(map(str,t))
                        t=int(t)
                        if res>t:
                            res=t
                    if n[ind]!=i and n[ind]!=j:
                        ok=False
                        break
                if ok:
                    res=n1
                            
        print(res)
                             