import os, sys
from io import BytesIO, IOBase
from copy import copy


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, 8192))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, 8192))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


class disjointset:
    def __init__(self, n):
        self.rank, self.parent, self.n = [0] * (n + 1), [i for i in range(n + 1)], n

    def find(self, x):
        xcopy = x
        while x != self.parent[x]:
            x = self.parent[x]

        while xcopy != x:
            self.parent[xcopy], xcopy = x, self.parent[xcopy]
        return x

    def union(self, x, y):
        xpar, ypar = self.find(x), self.find(y)
        if xpar == ypar:
            return

        par, child = xpar, ypar
        if self.rank[xpar] < self.rank[ypar]:
            par, child = ypar, xpar

        elif self.rank[xpar] == self.rank[ypar]:
            self.rank[xpar] += 1

        self.parent[child] = par
        self.n -= 1


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")
inp = lambda dtype: [dtype(x) for x in input().split()]
inp_2d = lambda dtype, n: [dtype(input()) for _ in range(n)]
inp_2ds = lambda dtype, n: [inp(dtype) for _ in range(n)]
inp_enu = lambda dtype: [(i, x) for i, x in enumerate(inp(dtype))]
inp_enus = lambda dtype, n: [[i] + inp(dtype) for i in range(n)]
ceil1 = lambda a, b: (a + b - 1) // b

n, m = inp(int)
dis, edges = disjointset(n), inp_2ds(int,m)
pre, suf = [(copy(dis.parent), copy(dis.rank), dis.n)], [copy(dis.parent)]

for u,v in edges:
    dis.union(u, v)
    pre.append((copy(dis.parent), copy(dis.rank), dis.n))

dis1 = disjointset(n)
for u, v in edges[::-1]:
    dis1.union(u, v)
    suf.append(copy(dis1.parent))

suf.reverse()
for _ in range(int(input())):
    l, r = inp(int)
    dis.parent, dis.rank, dis.n = copy(pre[l - 1][0]), copy(pre[l - 1][1]), pre[l - 1][2]
    dis1.parent = copy(suf[r])

    for i in range(1, n + 1):
        dis.union(dis.parent[i], dis1.parent[i])

    print(dis.n)
