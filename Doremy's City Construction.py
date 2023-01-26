import sys
input = lambda: sys.stdin.readline().rstrip('/r/n')

def solve():
	n = int(input())
	a = list(map(int, input().split()))
	a.sort()
	x = -1
	ans = 0
	c = 0
	for i in a:
		if i != x:
			ans = max(ans, c * (n - c))
			x = i
		c += 1
	print(max(ans, n // 2))

for _ in range(int(input())):
	solve()