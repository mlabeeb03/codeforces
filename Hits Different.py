import sys

try:
    file = open("inp.txt", "r")
    input = lambda: file.readline().rstrip("\n\r")
except:
    input = lambda: sys.stdin.readline().rstrip("\n\r")

# _____________________________________________________________


def ini():
    return int(input())


def inl():
    return [i for i in input().split()]


def inli():
    return [int(i) for i in input().split()]


def ins():
    return [i for i in input()]


def insi():
    return [int(i) for i in input()]


# _____________________________________________________________

from collections import Counter
from itertools import accumulate

# _____________________________________________________________

inf = float("inf")
mod = 1000000007

# _____________________________________________________________


def solve():
    n = ini()
    if n == 1:
        print(1)
        return
    r = rownum[n]
    curr = [colnum[n], colnum[n] - len(dp[rownum[n]])]
    ans = 0
    # print(curr)
    if curr[0] == 0:
        ans += dp[r][curr[1]]
    else:
        ans += dp[r][curr[1]] - dp[r][curr[0] - 1]
    # print(ans)
    for i in range(r - 1, -1, -1):
        # print(i)
        lef, rig = None, None
        if curr[0] == 0:
            lef = 0
        else:
            lef = curr[0] - 1
        if curr[1] == -1:
            rig = -1
        else:
            rig = curr[1] + 1
        curr = [lef, rig]
        # print(curr)
        if curr[0] == 0:
            ans += dp[i][curr[1]]
            # print(dp[i][curr[1]])
        else:
            ans += dp[i][curr[1]] - dp[i][curr[0] - 1]
            # print(dp[i][curr[1]] - dp[i][curr[0] - 1])
    print(ans)


dp = [[1]]
rownum = {}
colnum = {}
curr = 2
for i in range(1, 1500):
    col, newarr = 0, []
    for j in range(curr, curr + len(dp[-1]) + 1):
        newarr.append(j**2)
        rownum[j] = i
        colnum[j] = col
        curr += 1
        col += 1
    dp.append(list(accumulate(newarr)))

# import os, psutil

# process = psutil.Process()
# print(int(process.memory_info().rss // (1024 * 1024)))  # in bytes

# print(curr)
# for i in arr:
#     print(i)
# print()

# for i in dp:
#     print(i)
# print()


for x in range(int(input())):
    solve()
