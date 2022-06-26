n, q, k = map(int, input().split())
a = list(map(int, input().split()))
for __ in range(q):
    l, r = map(int, input().split())
    print(k + a[r-1] - a[l-1] - 2*(r - l) - 1)
 



