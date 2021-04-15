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
        tmp[0] += tmp[1]
        print(tmp[0])
