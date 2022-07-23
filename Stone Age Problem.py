n, q = map(int,input().split())
a = list(map(int,input().split()))
s = sum(a)
values = {i + 1: a[i] for i in range(n)}
default = 0
res = []
for i in range(q):
    query = list(map(int,input().split()))
    if query[0] == 1:
        i, x = query[1], query[2]
        s -= values.get(i, default)
        s += x
        values[i] = x
    else:
        x = query[1]
        s = x * n
        default = x
        values = {}
    res.append(s)
print(*res)

     