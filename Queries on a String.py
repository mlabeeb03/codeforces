import sys
input = lambda: sys.stdin.readline().rstrip("\n\r")
#file = open('inp.txt', 'r'); input = lambda: file.readline().rstrip("\n\r")
from collections import deque

def solve():
    s = list(map(str, input()))
    m = int(input())
    for i in range(m):
        l, r, k = list(map(int, input().split()))
        k %= r - l + 1
        #print(k)
        x = deque([])
        for j in range(r - 1, r - k - 1, -1):
            x.appendleft(s[j])
        for j in range(l - 1, r - k):
            x.append(s[j])
        for j in range(l - 1, r):
            s[j] = x.popleft()
        #print(s)
    print(''.join(i for i in s))

for _ in range(1):
    solve()
    
#abacaba
#3 6 1
#1 4 2