import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")

n, k = list(map(int, input().split()))
s = ''
for i in range(97, 97 + k):
    s += chr(i)
    for j in range(97, i)[::-1]:
        s += chr(i) + chr(j)
s = list(s)
ans = ['a']
while len(ans) < n:
    ans += s[:k * k]
print(''.join(ans[:n]))


print(s)
