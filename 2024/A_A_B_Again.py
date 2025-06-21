import sys

inp = "".join(sys.stdin.readlines()).strip().split("\n")[1:]
for i in inp:
    print(sum([int(i) for i in list(i)]))
