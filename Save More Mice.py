# -*- coding: utf-8 -*-

def solve(n, k, line):
    line.sort(reverse = True)
    sum = count = 0
    for i in range(k):
        if(sum + n - line[i] < n):
            sum += n - line[i]
            count += 1
    print(count)

tcs = int(input())
for i in range(tcs):
    n, k = list(map(int, input().split()))
    line = list(map(int, input().split()))
    solve(n, k, line)
    

    