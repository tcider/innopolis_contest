tmp = input().split()
if len(tmp) != 5:
    print("Wrong data")
for i in range(len(tmp)):
    try:
        tmp[i] = int(tmp[i])
        if i > 0:
            tmp[i] -= 1
    except:
        print("Wrong data")
arr = input().split()
if len(arr) != tmp[0]:
    print("Wrong data")
for i in range(len(arr)):
    try:
        arr[i] = int(arr[i])
    except:
        print("Wrong data")
n = 0
while True:
    first_stop = tmp[2] - tmp[1]
    if first_stop % 2:
        first_stop = (first_stop + 1) // 2
    else:
        first_stop //= 2
    for i in range(first_stop):
        num = arr[tmp[1] + i]
        arr[tmp[1] + i] = arr[tmp[2] - i]
        arr[tmp[2] - i] = num
    n += 1
    if n == 2:
        break
    tmp[1] = tmp[3]
    tmp[2] = tmp[4]

for i in range(tmp[0]):
    print(arr[i], end="")
    if i != tmp[0] - 1:
        print(" ", end="")