def isPalindrome(arr):
    for i in range(len(arr) // 2):
        if arr[i] != arr[len(arr)-i-1]:
            return False
    return True

def solve():
    n = int(input())
    #a = list(map(int, input().split()))
    #n, k = map(int, input().split())
    a = list(map(str, input()))
    
    for i in range(n // 2):
        if a[i] != a[n-i-1]:
            
            xc = yc = 0
            l, r = 0, n - 1
            while(l < r):
                if a[l] == a[i] and a[r] != a[i]:
                    xc += 1
                    l += 1
                    continue
                elif a[r] == a[i] and a[l] != a[i]:
                    xc += 1
                    r -= 1
                    continue
                else:
                    l += 1
                    r -= 1
                    
            l, r = 0, n - 1
            while(l < r):
                if a[l] == a[n-i-1] and a[r] != a[n-i-1]:
                    yc += 1
                    l += 1
                    continue
                elif a[r] == a[n-i-1] and a[l] != a[n-i-1]:
                    yc += 1
                    r -= 1
                    continue
                else:
                    l += 1
                    r -= 1
                    
            x = [j for j in a if j != a[i]]
            y = [j for j in a if j != a[n-i-1]]
            
            r1 = isPalindrome(x)
            r2 = isPalindrome(y)
            
            if r1 and r2:
                print(min(xc, yc))
            elif r1:
                print(xc)
            elif r2:
                print(yc)
            else:
                print(-1)
            return
    print(0)

for _ in range(int(input())):
    solve()

    