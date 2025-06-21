import sys


def calculateParticipator(theList, limit):
    theList.sort()
    total = sum(theList)
    if limit > total:
        return "infinite"
    pos = 0
    now = max(theList)
    while total > limit:
        point = len(theList) - 1
        theList = theList[:point]
        pos += 1
        now -= 1
        total = sum(theList) + pos * now
    return now


inp = "".join(sys.stdin.readlines()).strip().split("\n")
limit = int(inp[0].split()[1])
perticipateList = [int(i) for i in inp[1].split()]

# limit = 8
# perticipateList = [1, 3, 2, 4]

print(calculateParticipator(perticipateList, limit))
