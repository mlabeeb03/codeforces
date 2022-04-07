#import math
#def solve():

for _ in range(int(input())):
    n = int(input())
    #n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort(reverse = True)
    print(*arr)
    

    