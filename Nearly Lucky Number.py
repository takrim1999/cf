import sys
number = sys.stdin.readline()
n = number.count("4") + number.count("7")
if n == 4 or n == 7:
    print("YES")
else:
    print("NO")
