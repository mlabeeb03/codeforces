from itertools import accumulate

for _ in range(int(input())):
	n = int(input())
	a = list(map(int, input().split()))
	m = int(input())
	b = list(map(int, input().split()))
	arr = [0] + list(accumulate(a))
	brr = [0] + list(accumulate(b))
	ans = 0
	for i in range(n + 1):
		for j in range(m + 1):
			ans = max(ans, arr[i] + brr[j])
	print(ans)