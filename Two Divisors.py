import sys
input = lambda: sys.stdin.readline().rstrip("\n\r")
import math

lim = int(10 ** 7) + 1
mindiv = [math.inf for i in range(lim)]
mindiv[1] = 1
for i in range(2, lim):
    if mindiv[i] == math.inf:
        for j in range(1, lim):
            try:
                mindiv[i * j] = min(mindiv[i * j], i)
            except:
                break

n = int(input())
a = list(map(int, input().split()))
r1 = []
r2 = []
for i in a:
    u = mindiv[i]
    v = i
    while v % u == 0:
        v //= u
    if v == 1:
        r1.append(-1)
        r2.append(-1)
    else:
        r1.append(v)
        r2.append(i // v)
#print(*mindiv)
print(*r1)
print(*r2)

    