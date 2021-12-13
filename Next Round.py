n = int(input("").split()[1]) - 1
count = 0
inp = input("").split()
for i in inp:
    if int(i) >= int(inp[n]) and int(i)!=0:
        count = count + 1
print(count)
