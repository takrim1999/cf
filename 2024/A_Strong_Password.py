import sys


def insertion(str):
    strings = "abcdefghijklmnopqrstuvwxyz"
    present = point = 0
    next = 1
    if len(str) < 2:
        str = "".join(str)
        if strings[point] == str:
            point += 1
        return str + strings[point]
    while next != len(str):
        if str[present] == str[next]:
            if str[present] == strings[point]:
                point += 1
            str.insert(next, strings[point])
            return "".join(str)
        present += 1
        next += 1
    if str[present] == strings[point]:
        point += 1
    str.insert(next, strings[point])
    return "".join(str)


inp = "".join(sys.stdin.readlines()).strip().split("\n")[1:]
for i in inp:
    print(insertion(list(i)))

# print(insertion(list("aaa")))
