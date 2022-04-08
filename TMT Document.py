#import math
def solve():
    n = int(input())
    arr = list(map(str, input()))
    tarr = []
    marr = []
    
    if arr.count('T') != arr.count('M')*2:
        print('NO')
        return
    for i in range(n):
        if arr[i] == 'T':
            tarr.append(i)
        else:
            marr.append(i)
    
    for i in range(int(n/3)):
        if marr[i] < tarr[i] or marr[i] > tarr[i+int(n/3)]:
            print('NO')
            return
    print('YES')
    
        

for _ in range(int(input())):
    solve()

    