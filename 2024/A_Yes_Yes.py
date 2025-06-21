import sys


def validateYesNo(array):
    test = "Yes"
    arrayPointer = 0
    if array[0] == "Y":
        testPointer = 0
    elif array[0] == "e":
        testPointer = 1
    elif array[0] == "s":
        testPointer = 2
    else:
        return "NO"
    while arrayPointer != len(array):
        if array[arrayPointer] == test[testPointer]:
            testPointer += 1
        else:
            return "NO"
        if testPointer > 2:
            testPointer = 0
        arrayPointer += 1
    return "YES"


inp = "".join(sys.stdin.readlines()).strip().split("\n")[1:]
for i in inp:
    print(validateYesNo(i))

# print(validateYesNo("esYes"))
