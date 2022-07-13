for _ in range(int(input())):
    n = int(input())
    a = [int(item) for item in input().split()]
    b = [int(item) for item in input().split()]
    
    if all(a[i] <= a[i+1] for i in range(n - 1)):
        print('Yes')
        continue
    if b.count(1) > 0 and b.count(0) > 0:
        print('Yes')
        continue
    print('No')
    