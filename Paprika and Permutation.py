def solve():
    n = int(input())
    a = list(map(int, input().split()))   
    
    st = set()
    for i in range(1, n + 1):
        st.add(i)
        
    arr = []
    for i in a:
        if i in st:
            st.remove(i)
        else:
            arr.append(i)
            
    s = list(st)
    s.sort()
    
    arr.sort()
    for i in range(len(arr)):
        if s[i] >= arr[i] / 2:
            print(-1)
            return
        
    print(len(arr))
    
           
for _ in range(int(input())):
    solve()