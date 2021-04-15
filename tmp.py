



sum = 0
for i in range(size):
    subsum = arr[i]
    if not arr[i]:
        sum += 1
    for j in range(i + 1, size):
        subsum += arr[j]
        if not subsum % 2:
            sum += 1

print(sum)