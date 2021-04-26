string = input()

sum = 0
size = len(string)
for i in range(size):
    sum += int(string[i])

res = 0
for i in range(size):
    tmp = sum - int(string[i])
    if tmp % 3 == 0:
        res += 4
    else:
        res += 3

if sum % 3 == 0:
    res -= size - 1

print(res)