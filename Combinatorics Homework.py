for _ in range(int(input())):
	a, b, c, m = map(int, input().split())
	a, b, c = sorted([a, b, c])
	print("YES" if c - (a + b + 1) <= m <= a + b + c - 3 else "NO")

    