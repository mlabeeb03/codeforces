import sys
try:
    file = open('inp.txt', 'r')
    input = lambda: file.readline().rstrip("\n\r")
except:
    input = lambda: sys.stdin.readline().rstrip("\n\r")   

def bob(arr):
    # print(arr)
    n = len(arr)
    for i in range(n):
        if arr[i][0] == 'O' and arr[i][1] >= 3:
            return True
    for i in range(n - 2):
        if arr[i][0] == 'O' and arr[i + 1][1] == 1 and (arr[i][1] >= 2 or arr[i + 2][1] >= 2):
            return True
    return False

def solve():
    a = [i for i in input()]
    arr = [[a[0], 1]]
    for i in a[1:]:
        if i == arr[-1][0]:
            arr[-1][1] += 1
        else:
            curr = 'X'
            if arr[-1][0] == 'X': curr = 'O'
            arr.append([curr, 1])
    n = len(arr)
    for i in range(n):
        if arr[i][0] == 'X' and arr[i][1] >= 3:
            print('Alice')
            return
    for i in range(n - 2):
        if arr[i][0] == 'X' and arr[i + 1][1] == 1 and (arr[i][1] >= 2 or arr[i + 2][1] >= 2):
            print('Alice')
            return
    b = a[:]
    for i in range(len(a) - 1):
        a = b[:]
        a[i], a[i + 1] = a[i + 1], a[i]
        arr = [[a[0], 1]]
        for i in a[1:]:
            if i == arr[-1][0]:
                arr[-1][1] += 1
            else:
                curr = 'X'
                if arr[-1][0] == 'X': curr = 'O'
                arr.append([curr, 1])
        n = len(arr)
        if bob(arr) == False:
            print('Tie')
            return
    print('Bob')

for _ in range(int(input())):
    solve()

# 4
# XOXXO
# OOXOX
# OOXOXOXO
# XOXOX

