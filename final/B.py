params = input().split()
if len(params) != 3:
    params = params[0].split(',')
params[0] = int(params[0])
arr = input().split()
if len(arr) != params[0]:
    arr = arr[0].split(',')

num1 = 0
num2 = 0
for i in range(params[0]):
    if arr[i] == params[1]:
        num1 += 1
    elif arr[i] == params[2]:
        num2 += 1
i = params[0] - 1
while i >= 0 and num1 != num2:
    if arr[i] == params[1]:
        num1 -= 1
    elif arr[i] == params[2]:
        num2 -= 1
    i -= 1
print(i)


