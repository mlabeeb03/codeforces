def check(arr):
    return False if arr[0]%2 + arr[1]%2 + arr[2]%2 + arr[3]%2 > 1 else True
def check2(arr):
    return False if (arr[0]-1)%2 + (arr[1]-1)%2 + (arr[2]-1)%2 + (arr[3]+3)%2 > 1 else True
for _ in range(int(input())):
    arr = list(map(int, input().split()))
    if check(arr):
        print('Yes')
    elif arr[0]>0 and arr[1]>0 and arr[2]>0 and check2(arr):
        print('Yes')
    else:
        print('No')

    