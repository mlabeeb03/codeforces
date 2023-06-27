import sys
try:
    file = open('inp.txt', 'r')
    input = lambda: file.readline().rstrip("\n\r")
except:
    input = lambda: sys.stdin.readline().rstrip("\n\r")

def findlow(arr):
    n = len(arr)
    curr = arr.count(1)
    i = 0
    tb = 0
    while i + 1 < n and tb < n // 4:
        if arr[i] == 1 and arr[i + 1] == 1:
            curr -= 1
            i += 2
            tb += 1
        else:
            i += 1
    return curr

def findhigh(arr):
    n = len(arr)
    i = 0
    curr = arr.count(1)
    tb = 0
    while i + 1 < n and tb < n // 4:
        if arr[i] == 0 or arr[i + 1] == 0:
            i += 2
            tb += 1
        else:
            i += 1
    return curr - (n // 4 - tb)

def solve():
    n, m = map(int, input().split())
    low = 0
    high = 0
    for i in range(n):
        arr = [int(i) for i in input()]
        low += findlow(arr)
        high += findhigh(arr)
    print(low, high)
     
for _ in range(1):
    solve()
