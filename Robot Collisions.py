import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip("\n\r")
#file = open('inp.txt', 'r'); input = lambda: file.readline().rstrip("\n\r")

def bothLeft(p, q):
    return p + (q - p) // 2
def bothRight(p, q, r):
    return (r - q) + (r - (p + (r - q))) // 2
def do(arr, ans, r):
    rig = deque([])
    lef = deque([])

    for i in arr:
        if i[1] == 'L' and len(rig) > 0:
            ans[i[2]] = ans[rig[-1][2]] = abs(rig[-1][0] - i[0]) // 2
            rig.pop()
        elif i[1] == 'L':
            lef.append(i)
        else:
            rig.append(i)

    while len(lef) > 1:
        ans[lef[0][2]] = ans[lef[1][2]] = bothLeft(lef[0][0], lef[1][0])
        lef.popleft()
        lef.popleft()

    while len(rig) > 1:
        ans[rig[-1][2]] = ans[rig[-2][2]] = bothRight(rig[-2][0], rig[-1][0], r)
        rig.pop()
        rig.pop()

    if len(lef) > 0 and len(rig) > 0:
        x = None
        if lef[0][0] == r - rig[0][0]:
            x = lef[0][0] + r // 2
        elif lef[0][0] > r - rig[0][0]:
            x = r - rig[0][0] + bothLeft(lef[0][0] - (r - rig[0][0]), r)
        elif r - rig[0][0] > lef[0][0]:
            x = lef[0][0] + bothRight(0, rig[0][0] + lef[0][0], r)
        ans[lef[0][2]] = ans[rig[0][2]] = x

    #print(arr)
    #print(ans)
    #print()

def solve():
    n, r = map(int, input().split())
    a = list(map(int, input().split()))
    d = list(map(str, input().split()))
    
    ans = [-1] * n

    arr = []
    for i in range(n):
        if a[i] % 2 == 0:
            arr.append([a[i], d[i], i])
    arr.sort()
    do(arr, ans, r)

    arr = []
    for i in range(n):
        if a[i] % 2 == 1:
            arr.append([a[i], d[i], i])
    arr.sort()
    do(arr, ans, r)

    print(*ans)

for _ in range(int(input())):
    solve()
    