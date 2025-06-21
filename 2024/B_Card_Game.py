import sys

inp = "".join(sys.stdin.readlines()).strip().split("\n")[1:]

for i in inp:
    count = 0
    ocount = 0
    a1, a2, b1, b2 = [int(i) for i in i.split()]
    if a1 > b1:
        if a2 > b2:
            round = 2
        elif a2 < b2:
            round = 0
        else:
            round = 1

    elif a1 < b1:
        if a2 > b2:
            round = 0
        elif a2 < b2:
            round = -2
        else:
            round = -1

    elif a1 == b1:
        if a2 > b2:
            round = 1
        elif a2 < b2:
            round = -1
        else:
            round = 0

    if round < 0:
        print(0)
    else:
        print(round)

    # if a1>b2 and a2>b1:
    # for j, k in zip(i[:2], i[2:]):
    #     if j > k:
    #         count += 1
    #     elif k > j:
    #         ocount += 1
    # # print(count, ocount)
    # for j, k in zip(i[:2], i[::-1][:2]):
    #     if j > k:
    #         count += 1
    #     elif k > j:
    #         ocount += 1

    # if count - ocount < 0:
    #     print(0)
    # else:
    #     print(count - ocount)
