import sys
date = int(sys.stdin.readline())+1
while len(set(str(date)))!=4:
    date = date + 1
print(date)