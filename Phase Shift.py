import sys
input = lambda: sys.stdin.readline().rstrip('\r\n')

def solve():
	n = int(input())
	a = list(map(str, input()))
	dic = {}
	par = {}
	for i in range(1, 27):
		dic[chr(i + 96)] = 0
		par[chr(i + 96)] = chr(i + 96)
	unused = [chr(i) for i in range(26 + 96, 0 + 96, -1)]

	for i in a:
		if dic[i] == 0:
			if len(unused) == 1:
				dic[i] = unused.pop()
				break
			else:
				for j in range(len(unused) - 1, -1, -1):
					if par[unused[j]] != par[i]:
						dic[i] = unused[j]
						par[unused[j]] = par[i]
						for k in par:
							if par[k] == unused[j]:
								par[k] = par[i]
						unused.remove(unused[j])
						break
		#print(i, dic[i])
	for i in a:
		print(dic[i], end = '')
	print()

for _ in range(int(input())):
	solve()