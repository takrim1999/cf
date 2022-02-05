import sys
numbers = sys.stdin.readline().strip().split("+")
numbers.sort()
print("+".join(numbers))