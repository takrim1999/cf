import sys
words = sys.stdin.readlines()
if words[0][:-1] == words[1][:-1:][::-1]:
    print("YES")
else:
    print("NO")