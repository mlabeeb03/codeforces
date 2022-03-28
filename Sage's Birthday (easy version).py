# -*- coding: utf-8 -*-

n = int(input())
prices = list(map(int, input().split()))
ind = 0
# n/2 to end are not cheap
if n%2 == 1:
    print(int(n/2))
else:
    print(int(n/2 - 1))

prices.sort()
listCheap = prices[:int(n/2)]
listExpensice = prices[int(n/2):]
finalList = []

for i in range(int(n/2) + 1):
    try:
        finalList.append(listExpensice[i])
        finalList.append(listCheap[i])
    except:
        continue

print(*finalList)
        


    