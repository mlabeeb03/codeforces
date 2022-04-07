arr = []
t = int(input())
for _ in range(t):
    arr.append(input())
x = arr.count(arr[0])
if x > int(t/2):
    print(arr[0])
else:
    for i in range(t):
        if arr[i] != arr[0]:
            print(arr[i])
            break

        

    