def solve():
    n = int(input())
    nums = list(map(int, input().split()))
    if n == 1:
        if nums[0] > 1:
            print('No')
        else:
            print('YES')
        return
    
    nums.sort(reverse = True)
    if nums[0] - nums[1] > 1:
        print('No')
    else:
        print('YES')
    
for _ in range(int(input())):
    solve()
    



