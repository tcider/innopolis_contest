tmp = input().split()
if len(tmp) != 2:
    print("Wrong data")
else:
    try:
        tmp[0] = int(tmp[0])
        tmp[1] = int(tmp[1])
    except:
        print("Wrong data")
    else:
        if tmp[1] > tmp[0]:
            for i in range(tmp[0], tmp[1] + 1):
                print(i, end="")
                if i != tmp[1]:
                    print(" ", end="")
        else:
            while tmp[0] >= tmp[1]:
                print(tmp[0], end="")
                if tmp[0] != tmp[1]:
                    print(" ", end="")
                tmp[0] -= 1
