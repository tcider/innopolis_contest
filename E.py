size = int(input())
arr = input().split()
for i in range(size - 1):
    arr[i] = int(arr[i])
arr.sort()
if arr[0] > 1:
    res = 1
else:
    for i in range (1, size - 1):
        if arr[i] - arr[i - 1] > 1:
            res = arr[i] - 1
            break
        res = arr[size - 2] + 1
print(res)