for _ in range(int(input())):
    n = int(input())
    #a = list(map(int, input().split()))
    a = list(map(int, input()))
    x = a.count(0)
    if x == 1 or x % 2 == 0:
        print('BOB')
    else:
        print('ALICE')


