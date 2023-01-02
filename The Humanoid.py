import sys
input = lambda: sys.stdin.readline().rstrip("\n\r")

def solve():
    #n = int(input())
    n, p = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    
    lst = []
    avb = []
    for j in range(3):
        if j == 0:
            avb = [2, 2, 3]
        elif j == 1:
            avb = [2, 3, 2]
        elif j == 2:
            avb = [3, 2, 2]
        ans = 0
        did = 0
        h = p
        for i in range(n):
            if a[i] < h:
                ans += 1
                h += a[i] // 2
            else:
                while a[i] >= h and len(avb) > 0:
                    h *= avb.pop()
                if a[i] < h:
                    ans += 1
                    h += a[i] // 2
                else:
                    lst.append(ans)
                    #print('here', j, lst)
                    did = 1
                    break
        if did == 0:
            #print('there', j, lst)
            lst.append(ans)
            
    print(max(lst))

for _ in range(int(input())):
    solve()
