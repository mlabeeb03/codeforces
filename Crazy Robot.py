import sys
input = lambda: sys.stdin.readline().rstrip("\n\r")

def choices(arr, r, c):
    ch = 0
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        if arr[r + dx][c + dy] == '.':
            ch += 1
    return ch

def available(arr, r, c):
    if arr[r][c] == '.':
        return True
    return False
    
def solve():  
    n, m = list(map(int, input().split()))
    arr = []
    arr.append(['#'] * (m + 2))
    for i in range(n):arr.append(['#'] + list(map(str, input())) + ['#'])
    arr.append(['#'] * (m + 2))
    
    stack = []
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if arr[i][j] == 'L':
                stack.append((i, j))
                break
        else:
            continue
        break
    
    while stack:
        a, b = stack.pop()
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if available(arr, a + dx, b + dy) and choices(arr, a + dx, b + dy) < 2:
                arr[a + dx][b + dy] = '+'
                stack.append((a + dx, b + dy))
    
    for i in range(1, len(arr) - 1):
        print(''.join(x for x in arr[i][1:-1]))
    

for _ in range(int(input())):
    solve()


    