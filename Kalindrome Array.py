def is_palin(arr):
    n = len(arr)
    flag = 0;
    i = 0;
    while (i <= n // 2 and n != 0):
        if (arr[i] != arr[n - i - 1]):
            flag = 1;
            break;
        i += 1;
    if (flag == 1):
        return False;
    else:
        return True;

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    if n < 3:
        print('YES')
        return
    
    l = 0
    r = n - 1
    x = 0
    y = 0
    while(l < r):
        if a[l] != a[r]:
            x = a[l]
            y = a[r]
            break
        l += 1
        r -= 1
    if x == 0:
        print('YES')
        return
    b = [z for z in a if z != x]
    c = [z for z in a if z != y]
    if is_palin(b) or is_palin(c):
        print('YES')
        return
    print('NO')
    

for _ in range(int(input())):
    solve()

    