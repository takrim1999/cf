import sys
strings = sys.stdin.readlines()[1:]
for i in strings:
    print(2**int(i[:-1])-1)