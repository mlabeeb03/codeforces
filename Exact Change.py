import sys
input = lambda: sys.stdin.readline().rstrip("\n\r")

def solve():
    n = int(input())  
    a = list(map(int, input().split()))
    mx = max(a)
    ans = mx
    
    for u in range(3):
        for d in range(3):
            arr = []
            for x in range(u + 1):
                for y in range(d + 1):
                    arr.append(y * 2 + x)
            arr.sort(reverse = True)
            #print('u d arr:', u, d, arr)
            t = 0
            done = 0
            temp = 0
            for i in a:               
                for j in arr:
                    #print('here', i, j)
                    if i - j >= 0 and (i - j) % 3 == 0:
                        #print('inside')
                        t = max(t, (i - j) // 3)
                        #print(t)
                        temp = max(temp, u + d + t)
                        done += 1
                        #print('ans done:',ans, done)
                        break
            if done == n:
                ans = min(ans, temp)
            #print(t, ans)
    print(ans)
            
for _ in range(int(input())):
    solve()


    