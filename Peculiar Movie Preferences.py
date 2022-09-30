import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")

def solve():
    n = int(input())
    #n, m = map(int, input().split())    
    #a = list(map(int, input().split()))
    setof2 = set()
    setof3 = set()
    setof3but2 = set()
    arr = []
    for i in range(n):
        arr.append(list(map(str, input())))
    #print(arr)
    for i in range(n):
        a = arr[i]
        if len(set(a)) == 1:
            print('YES')
            return
        else:
            if len(a) == 2:
                if (a[1], a[0]) in setof2 or (a[1], a[0]) in setof3but2:
                    print('YES')
                    return
                else:
                    setof2.add((a[0], a[1]))
            else:
                if (a[2], a[1]) in setof2 or (a[2], a[1], a[0]) in setof3 or a[0] == a[2]:
                    print('YES')
                    return
                else:
                    setof3.add((a[0], a[1], a[2]))
                    setof3but2.add((a[0], a[1]))
    print('NO')

for _ in range(int(input())):
    solve()

    