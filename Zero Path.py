import sys
input = lambda: sys.stdin.readline().rstrip('\r\n')
from copy import deepcopy

def solve():
	n, m = list(map(int, input().split()))
	arr = []
	for i in range(n):
		arr.append(list(map(int, input().split())))
	if (n + m) % 2 == 0:
		print('NO')
		return
	dpmin = deepcopy(arr)
	dpmax = deepcopy(arr)
	dpmin[0][0] = dpmax[0][0] = arr[0][0]
	for i in range(n):
		for j in range(m):
			if i == 0 and j == 0:
				continue
			if i == 0:
				dpmin[i][j] = dpmax[i][j] = arr[i][j] + dpmin[i][j - 1]
			elif j == 0:
				dpmin[i][j] = dpmax[i][j] = arr[i][j] + dpmin[i - 1][j]
			else:
				dpmin[i][j] = arr[i][j] + min(dpmin[i - 1][j], dpmin[i][j - 1])
				dpmax[i][j] = arr[i][j] + max(dpmax[i - 1][j], dpmax[i][j - 1])
	#for i in arr: print(i)
	#print(dpmin, dpmax)
	if dpmin[n - 1][m - 1] > 0 or dpmax[n - 1][m - 1] < 0:
		print('NO')
	else:
		print('YES') 

for _ in range(int(input())):
	solve()