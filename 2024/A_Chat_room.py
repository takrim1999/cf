import sys


def checkMessage(message):
    checkText = "hello"
    checkPoint = 0
    point = 0
    # return message

    while point < len(message):
        # print(message[point])
        if message[point] == checkText[checkPoint]:
            try:
                if message[point] == message[point + 1]:
                    if checkText[checkPoint] == checkText[checkPoint + 1]:
                        checkPoint += 1
            except:
                pass
            else:
                checkPoint += 1
        if checkPoint == len(checkText):
            return "YES"
        point += 1
    return "NO"


inp = "".join(sys.stdin.readlines()).strip().split("\n")[0]
# inp = "hlelo"
# inp = "ahhellllloou"

print(checkMessage(inp))
