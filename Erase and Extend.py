import sys
input = sys.stdin.readline

def pprint(mn):
    for i in mn:
        print(i, end = '')
    print()
def get(s, k):
    while len(s) < k:
        s += s
    while len(s) > k:
        s.pop()
    return s

n, x = map(int, input().split())    
a = list(input())

i = 1
j = n 
while i < n:
    if a[i] > a[0]:
        j = i
        break
    elif a[i] == a[0]:
        k = i
        l = 0
        while k < n and a[k] == a[l]:
            k += 1
            l += 1
        if k >= n or a[k] > a[l]:
            j = i
            break
        else:
            i = k
    else:
        i += 1  
pprint(get(a[:j], x))

