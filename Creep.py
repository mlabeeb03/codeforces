def solve():
    a, b = map(int, input().split())    
    if a == b:
        print('10' * a)
    elif a > b:
        print('0' * (a - b), end = '')
        print('10' * b)
    else:
        print('1' * (b - a), end = '')
        print('01' * a)

for _ in range(int(input())):
    solve()

    