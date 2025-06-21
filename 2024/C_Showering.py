import sys


def Remove(mainList, subList):
    newList = [i for i in mainList if i not in subList]
    return newList


test = input("")

for _ in range(int(test)):
    flag = False
    n, s, t = sys.stdin.readline().split()
    # print(n, s, t)
    n = int(n)
    count = 0
    day = list(range(int(t) + 1))
    # print(day)
    while n != 0:
        a, b = [int(el) for el in sys.stdin.readline().split()]
        day = Remove(day, list(range(a, b + 1)))
        n -= 1
    print(day)
    for i in range(len(day) - 1):
        if day[i + 1] == day[i] + 1:
            count += 1
        print(count + 1)
        print("s", int(s))
        if count + 1 >= int(s) - 1:
            flag = True
    if flag:
        print("YES")
    else:
        print("NO")
