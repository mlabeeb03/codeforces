import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")

def solve():
    a = list(map(int, input()))
    n = len(a)
    lst = [0] * 10
    for i in a:
        lst[i] += 1
    fin = [0] * 10
    curr = 0
    #print(lst)
    for i in range(n):
        if lst[curr] == 0:
            while curr <= 9 and lst[curr] == 0:
                curr += 1
        if a[i] == curr:
            lst[curr] -= 1
            fin[curr] += 1
            while curr <= 9 and lst[curr] == 0:
                curr += 1
        else:
            lst[a[i]] -= 1
            fin[min(a[i] + 1, 9)] += 1
    #print(fin)
    for i in range(10):
        if fin[i] > 0:
            print(str(i) * fin[i], end = '')
    print()
    

for _ in range(int(input())):
    solve()

    