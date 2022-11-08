import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")
 
def solve():
    n = int(input())
    arr = [0] + list(map(int, input().split())) 
    ans = 0
    st = set()
    lst = [0] * (n + 1)
    remind = []
    remppl = []
    for i in range(1, n + 1):
        if arr[i] not in st:
            lst[i] = arr[i]
            st.add(arr[i])
            ans += 1
        else:
            remind.append(i)
    for i in range(1, n + 1):
        if i not in st:
            remppl.append(i)
    
    for i in range(len(remind) - 1):
        if remind[i] != remppl[i]:
            lst[remind[i]] = remppl[i]
        else:
            lst[remind[i]] = remppl[i + 1]
            remppl[i + 1] = remppl[i]
    if len(remind) > 0:
        if remind[-1] == remppl[-1]:
            x = lst.index(arr[remind[-1]])
            lst[x] = remind[-1]
            lst[remind[-1]] = arr[remind[-1]]
        else:
            lst[remind[-1]] = remppl[-1]
    print(ans)
    print(*lst[1:])
    
for _ in range(int(input())):
    solve()