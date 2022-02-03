import sys
statements = sys.stdin.readlines()
count = 0
for i in statements[1:]:
    if "++" in i:
        count = count + 1
    elif "--" in i:
        count = count - 1
    else:
        pass
print(count)