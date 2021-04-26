size = int(input())
arr = input().split()
if len(arr) != size:
    arr = arr[0].split(',')

sum1 = 0
sum2 = 0

for i in range(size):
    arr[i] = int(arr[i])
    if i % 2:
        sum1 += 1 - arr[i]
        sum2 += arr[i]
    else:
        sum1 += arr[i]
        sum2 += 1 - arr[i]

print(min(sum1, sum2))