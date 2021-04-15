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
        res = tmp[0] * tmp[0] + tmp[1] * tmp[1]
        print(res)
