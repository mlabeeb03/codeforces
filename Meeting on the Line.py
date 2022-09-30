import math
import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")

def solve():
    ppl = int(input())
    pos = list(map(int, input().split()))
    dres = list(map(int, input().split()))
    minpos = math.inf
    maxpos = 0
    for i in range(ppl):
        minpos = min(minpos, pos[i] - dres[i])
        maxpos = max(maxpos, pos[i] + dres[i])
    print((minpos + maxpos) / 2)
    
for _ in range(int(input())):
    solve()

    