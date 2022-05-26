def findmin(arr):
    sa = 0
    sb = 0
    ra = 5
    rb = 5
    for i in range(10):
        if arr[i] == '1' and i%2 == 0:
            sa += 1
        if i%2 == 0:
            ra -= 1
        if sa > sb+rb or sb > sa+ra:
            return 10 -(ra+rb)
        if arr[i] == '1' and i%2 == 1:
            sb += 1
        if i%2 == 1:
            rb -= 1
        if sa > sb+rb or sb > sa+ra:
            return 10 -(ra+rb)
    return 10

def solve(arr):
    res = [10, 10]
    a = arr[:]
    b = arr[:]
    
    for i in range(0, 10, 2):
        if a[i] == '?':
            a[i] = '1'
        if b[i] == '?':
            b[i] == '0'
    for i in range(1, 9, 2):
        if a[i] == '?':
            a[i] = '0'
        if b[i] == '?':
            b[i] = '1'
            
    res[0] = findmin(a)
    res[1] = findmin(b)
    return res

for _ in range(int(input())):
    arr = list(input())
    print(min(solve(arr)))



