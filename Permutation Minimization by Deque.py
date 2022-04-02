from collections import deque
for i in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    d = deque()
    for i in nums:
        if not d or i < d[0]:
            d.appendleft(i)
        else:
            d.append(i)
    print(*d)
    