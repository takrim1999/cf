import sys
count = 0
things = sys.stdin.readlines()
for i in range(int(things[0])):
    if things[1][i] == things[1][i+1]:
        count = count + 1 
    else:
        pass
print(count)