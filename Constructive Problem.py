import sys
try:
    file = open('inp.txt', 'r')
    input = lambda: file.readline().rstrip("\n\r")
except:
    input = lambda: sys.stdin.readline().rstrip("\n\r")

# _____________________________________________________________

def ini():
    return(int(input()))
def inl():
    return([i for i in input().split()])
def inli():
    return([int(i) for i in input().split()])
def ins():
    return([i for i in input()])
def insi():
    return([int(i) for i in input()])

# _____________________________________________________________

from math import inf

# _____________________________________________________________

def mex(a):
    s = set(a)
    for i in range(2000005):
        if i not in s:
            return i

def solve():
    n = ini()
    a = inli()
    req = mex(a) + 1
    # print(req)
    have = set()
    spare = 0
    lef = 0
    for i in range(n):
        if a[i] != req:
            if a[i] in have:
                spare += 1
            elif a[i] < req:
                have.add(a[i])
            lef += 1
        else:
            break
    rig = n - 1
    for j in range(n - 1, lef, -1):
        if a[j] != req:
            if a[j] in have:
                spare += 1
            elif a[j] < req:
                have.add(a[j])
            rig -= i
        else:
            break
    notin = n - (len(have) + spare)
    # print(have, spare, notin)
    if len(have) == req:
        print('Yes')
    elif len(have) == req - 1:
        if spare > 0 or notin > 0:
            print('Yes')
        else:
            print('No')
    else:
        print('No')

for _ in range(int(input())):
    solve()
