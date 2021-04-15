size = int(input())
arr = input().split()
for i in range(size):
    if int(arr[i]) % 2:
        arr[i] = 1
    else:
        arr[i] = 0

last = 0
sum = 0
nechet = 0
nsum = 0
i = size - 1
while i >= 0:
    if not arr[i] % 2:
        last += 1
    else:
        if not nechet:
            nsum = last + 1
            last = 0
            nechet = 1
        else:
            last = nsum
            nsum = size - i - last
            #nechet = 0
    sum += last
    i -= 1
print(sum)