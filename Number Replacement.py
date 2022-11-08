import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")
 
def solve():
    n = int(input())
    #n, k = map(int, input().split())
    a = list(map(int, input().split()))
    s = list(map(str, input()))
    
    arr = []
    for i in range(51):
        arr.append([])
        
    for i in range(n):
        arr[a[i]].append(s[i])
        
    for i in range(51):
        if len(arr[i]) > 0 and len(set(arr[i])) > 1:
            print('NO')
            return
    print('YES')
    
                                   
for _ in range(int(input())):
    solve()