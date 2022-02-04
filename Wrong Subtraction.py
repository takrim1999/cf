import sys
number = sys.stdin.readline().split()
n = int(number[0])
for i in range(int(number[1])):
    if str(n)[-1] == "0":
        n = int(n/10)
    else:
        n = n - 1
print(n)