n, q = map(int, input().split())
a = list(map(int, input().split()))
t = list(map(int, input().split()))

arr = []

for i in range(q):
    try:
        x = arr.index(t[i])
        print(x+1, end = ' ')
        arr.remove(t[i])
        arr = [t[i]] + arr
    except:
        for j in range(n):
            if t[i] == a[j]:
                print(j+1, end = ' ')
                arr = [a[j]] + arr
                a = [a[j]] + a[:j] + a[j+1:]
                break


        



    