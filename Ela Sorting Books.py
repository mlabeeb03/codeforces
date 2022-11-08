import sys
input = lambda: sys.stdin.readline().rstrip("\r\n")

def solve():
    n, k = map(int, input().split())
    a = list(map(str, input()))
    arr = [0] * 26
    ans = []
    for i in a:
        arr[ord(i) - 97] += 1
    for i in range(k):
        done = 0
        for j in range(26):
            if arr[j] == 0 or done == n // k:
                ans.append(chr(j + 97))
                break
            arr[j] -= 1
            done += 1
    print(''.join(ans))      
    
      
for _ in range(int(input())):
    solve()