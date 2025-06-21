import sys

inp = "".join(sys.stdin.readlines()).strip().split("\n")

inp = int(inp[0])
# inp = 1992

if inp % 400 == 0:
    print(366)
if inp % 4 != 0:
    print(365)
if (inp % 100 != 0) and (inp % 4 == 0):
    print(366)
if (inp % 100 == 0) and (inp % 400 != 0):
    print(365)
