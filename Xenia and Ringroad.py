for _ in range(1):
	n, m = list(map(int, input().split()))
	a = list(map(int, input().split()))
	ans = 0
	pos = 1
	for i in a:
		if i == pos:
			continue
		elif i > pos:
			ans += i - pos
			pos = i
		elif i < pos:
			ans += (n - pos) + 1
			ans += i - 1
			#print('status',n, i, (n - i) + 1, i - 1)
			pos = i 
		#print(ans, pos)
	print(ans)