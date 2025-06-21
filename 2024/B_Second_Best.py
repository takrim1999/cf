import sys

inp = "".join(sys.stdin.readlines()).strip().split("\n")[1:]

nList = [int(i) for i in inp[0].split()]
second = sorted(nList, reverse=True)[1]
# print(nList)
# print(second)
print(nList.index(second) + 1)
