import sys

inp = "".join(sys.stdin.readlines()).strip().split("\n")

result, string = int(inp[0]) + int(inp[1].split()[0]) + int(inp[1].split()[1]), inp[2]
print(result, string)
